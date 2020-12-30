dataset = {
            "imgpath" : "/media/files/datasets/physionet.org/files/mimic-cxr-jpg/2.0.0/files",
            "csvpath" : "/media/files/datasets/physionet.org/files/mimic-cxr-jpg/2.0.0/mimic-cxr-2.0.0-chexpert.csv",
            "metacsvpath" : "/media/files/datasets/physionet.org/files/mimic-cxr-jpg/2.0.0/mimic-cxr-2.0.0-metadata.csv",
            "mode" : "PER_STUDY",
            "pathologies" : [
                "Enlarged Cardiomediastinum",
                "Cardiomegaly",
                "Lung Opacity",
                "Lung Lesion",
                "Edema",
                "Consolidation",
                "Pneumonia",
                "Atelectasis",
                "Pneumothorax",
                "Pleural Effusion",
                "Pleural Other",
                "Fracture",
                "Support Devices"],
            "views": ["PA"],
            "seed": 0,
            "transforms": {
                "train": [
                    ("ToPILImage", {}),
                    ("RandomAffine", {
                        "degrees": (-5, 5),
                        "shear": (0.9, 1.1)
                    }),
                    ("RandomResizedCrop", {
                        "size": (256, 256),
                        "scale": (0.5, 0.75),
                        "ratio": (0.95, 1.05),
                        "interpolation": 1
                    }),
                    ("ToTensor", {}),
                    ("Normalize", {
                        "mean": (0.4,),
                        "std": (0.2,)
                    })
                ],
                "test": [
                    ("ToPILImage", {}),
                    ("Resize", {
                        "size": 256,
                        "interpolation": 1
                    }),
                    ("CenterCrop", {
                        "size": 256
                    }),
                    ("ToTensor", {}),
                    ("Normalize", {
                        "mean": (0.4,),
                        "std": (0.2,)
                    })
                ]
            }

        }
