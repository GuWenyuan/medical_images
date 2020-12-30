import torch
import argparse

from texar.torch.run import (
    Executor,
    cond,
    metric,
    action
)

from data.MIMIC_CXR import MIMICCXR_Dataset
from data.config_mimic_cxr import dataset as hparams_dataset

from model.resnet import ResNet


# args
parser = argparse.ArgumentParser(description="Train MIMIC model")
parser.add_argument(
    '--save_dir',
    type=str,
    help='Place to save training results',
    default='exp_default/'
)
parser.add_argument(
    '--grad_clip',
    type=float,
    help='Gradient clip value',
    default=None
)
parser.add_argument(
    '--display_steps',
    type=int,
    help='log result every * steps',
    default=100
)
parser.add_argument(
    '--max_train_steps',
    type=int,
    help='Maximum number of steps to train',
    default=1000000
)
args = parser.parse_args()

# Dataloader
dataset = MIMICCXR_Dataset(hparams_dataset)

# model
model = ResNet()


# Trainer
executor = Executor(
    model=model,
    train_data=datasets["train"],
    valid_data=datasets["dev"],
    test_data=datasets["test"],
    checkpoint_dir=args.save_dir,
    save_every=cond.validation(better=True),
    train_metrics=("loss", metric.RunningAverage(args.display_steps)),
    optimizer={"type": torch.optim.Adam},
    grad_clip=args.grad_clip,
    log_every=cond.iteration(args.display_steps),
    validate_every=cond.epoch(1),
    valid_metrics=[
        metric.PearsonR(pred_name="preds"),
        ("loss", metric.Average())],
    plateau_condition=[
        cond.consecutive(cond.validation(better=False), 2)],
    action_on_plateau=[
        action.early_stop(patience=2),
        action.reset_params(),
        action.scale_lr(0.8)],
    stop_training_on=cond.iteration(args.max_train_steps),
    test_mode='eval',
)

executor.train()