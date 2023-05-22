from singleton_meta import SingletonMeta

class CleanConfig(metaclass=SingletonMeta):
    """
    Object that contains the parameters for the detection algorithm
    :params: category       category of the objects to detect, int
    :params: confidence     min confidence to accept, float
    """
    def __init__(self) -> None:

        self.FILENAME = "../None.csv"
        self.MODEL_REGISTRY = "../models"
        self.CATEGORICAL_COLS = [
            "merchant_group",
            "name_in_email",
        ]
        self.BOOL_COLS = 0.15
        self.TARGET = "default"
        self.MAJ_CLASS = 0
        self.MIN_CLASS = 1

        self.MANUAL_COL_DROP =  ["num_arch_ok_0_12m", 
                                'status_2nd_last_archived_0_24m',
                                'status_3rd_last_archived_0_24m',
                                'status_max_archived_0_6_months',
                                'status_max_archived_0_12_months',
                                'status_max_archived_0_24_months', 
                                'sum_capital_paid_account_0_12m', 
                                'sum_capital_paid_account_12_24m',
                                'sum_paid_inv_0_12m', "has_paid",
                                "merchant_category"
                                ]