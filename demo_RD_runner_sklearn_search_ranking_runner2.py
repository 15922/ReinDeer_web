import time
import os
from ReinDeer.utils import check_path_exist
from ReinDeer.RD_Sklearn.sklearn_base import SklearnStage
from ReinDeer.RD_stage_config import RDStageConfig
from ReinDeer.RD_pipeline import RDPipeline

# ============================================            stage 1            ===========================================

stage_param_dict1 = {
    'degree': 2,
    'interaction_only': False,
    'first_degree': False
}

stage1_config_dict = {
    'stage_backend': 'python1',  # sklearn, spark, tensorflow
    'stage_name': 'PolynomialFeaturesTransformer',
    'stage_param_dict': stage_param_dict1,
}

# ============================================            stage 2            ===========================================
stage_param_dict2 = {
}

stage2_config_dict = {
    'stage_backend': 'python2',  # sklearn, spark, tensorflow
    'stage_name': 'PairwiseSampleTransformer',
    'stage_param_dict': stage_param_dict2,
    'stage_user_defined_feature_columns_name': ['f1', 'f2', 'f3', 'f4', 'stage1_PolynomialFeaturesTransformer']

}

# ============================================            stage 3            ===========================================
stage_param_dict3 = {
    'feature_range': (0, 1),
}

stage3_config_dict = {
    'stage_backend': 'python3',  # sklearn, spark, tensorflow
    'stage_name': 'MaxMinScalar',
    'stage_param_dict': stage_param_dict3,
    'stage_user_defined_feature_columns_name': ['stage2_PairwiseSampleTransformer']

}

# ============================================            stage 4            ===========================================

stage_param_dict4 = {
    'train_sample_percentage': 0.8,
    'model_param': {'max_iter': 5, 'loss': 'log', 'alpha': 1e-6, 'n_jobs': -1, 'fit_intercept': True},
    'enable_grid_search_cv': False,  # 是否使用cross validation、grid search
    'grid_search_param': {     # grid search的参数
        'param_grid': {'max_iter': [5], 'alpha': [1e-4, 1e-5, 1e-6, 1e-7]},
        'scoring': 'accuracy',
        'cv': 3,  # k-fold中k的取值
        'iid': True
    }
}

stage4_config_dict = {
    'stage_backend': 'python4',
    'stage_name': 'SklearnPairwiseL2REstimator',  # sklearn, spark, tensorflow
    'stage_param_dict': stage_param_dict4,
    'stage_user_defined_feature_columns_name': ['stage3_MaxMinScalar']
}

# ============================================          RD Pipeline          ===========================================

pipeline_stages_config_dict = [stage1_config_dict, stage2_config_dict, stage3_config_dict, stage4_config_dict]

pipeline_config_dict = {
    'pipeline_uid': '2018122801',
    'root_directory': './sklearn_search_ranking_root_directory/',
    'root_data_directory': './sklearn_search_ranking_root_directory/data',
    'pipeline_input_format': 'file',
    'pipeline_input_file_name': 'data_eval',
    'pipeline_input_file_format': 'csv',
    'pipeline_input_feature_columns_name': ['f1', 'f2', 'f3', 'f4'],
    'pipeline_input_label_columns_name': ['label'],
    'pipeline_stages_config_dict': pipeline_stages_config_dict,
    'sampleID': 'sampleID',
    'groupID': 'groupID'
}


def pipeline_API_demo():
    print('pipeline ini')
    pipeline = RDPipeline(pipeline_config_dict)
    print('pipeline run')
    pipeline.run()


if __name__ == '__main__':
    print("pipeline API demo")
    print('train phase')
    pipeline_config_dict['pipeline_input_file_name'] = 'data_train'
    pipeline_config_dict['pipeline_phase_config'] = 'train'
    pipeline_API_demo()
    print('eval phase')
    pipeline_config_dict['pipeline_input_file_name'] = 'data_eval'
    pipeline_config_dict['pipeline_phase_config'] = 'eval'
    pipeline_API_demo()

