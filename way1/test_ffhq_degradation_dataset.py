import cv2
import numpy as np
import pytest
import yaml
from FFHQDegradationDataset import FFHQDegradationDataset
#from gfpgan.data.ffhq_degradation_dataset import FFHQDegradationDataset


def test_ffhq_degradation_dataset():

    with open('./test_ffhq_degradation_dataset.yml', mode='r') as f:
        opt = yaml.load(f, Loader=yaml.FullLoader)
        #print(opt)
    dataset = FFHQDegradationDataset(opt)

    assert dataset.io_backend_opt['type'] == 'disk'  # io backend
    print("-----------------------------------------")
    #print(len(dataset))
    #assert len(dataset) == 1  # whether to read correct meta info
    assert dataset.kernel_list == ['iso', 'aniso']  # correct initialization the degradation configurations
    assert dataset.color_jitter_prob == 1
    for i in range(len(dataset)):
    # test __getitem__
        result = dataset.__getitem__(i)
    #print(result)
    #res = result['lq']
    #res = res.numpy().transpose([1,2,0])
    #res = (res*255).astype(np.uint8)
    #cv2.imshow('a',res)
    #res[res<0] = 0
    #cv2.imwrite('./aaaa.png',res)
    #cv2.waitKey()
    #print(res)
    #print(res.shape)
    # check returned keys
    #expected_keys = ['gt', 'lq', 'gt_path']
    #assert set(expected_keys).issubset(set(result.keys()))
    # check shape and contents


    #assert result['gt'].shape == (3, 512, 512)
    #assert result['lq'].shape == (3, 512, 512)
    #assert result['gt_path'] == 'tests/data/gt/00000000.png'

    # ------------------ test with probability = 0 -------------------- #
#     opt['color_jitter_prob'] = 0
#     opt['color_jitter_pt_prob'] = 0
#     opt['gray_prob'] = 0
#     opt['io_backend'] = dict(type='disk')
#     dataset = FFHQDegradationDataset(opt)
#     assert dataset.io_backend_opt['type'] == 'disk'  # io backend
#     assert len(dataset) == 1  # whether to read correct meta info
#     assert dataset.kernel_list == ['iso', 'aniso']  # correct initialization the degradation configurations
#     assert dataset.color_jitter_prob == 0
#
#     # test __getitem__
#     result = dataset.__getitem__(0)
#     # check returned keys
#     expected_keys = ['gt', 'lq', 'gt_path']
#     assert set(expected_keys).issubset(set(result.keys()))
#     # check shape and contents
#     assert result['gt'].shape == (3, 512, 512)
#     assert result['lq'].shape == (3, 512, 512)
#     assert result['gt_path'] == 'tests/data/gt/00000000.png'
#
#     # ------------------ test lmdb backend -------------------- #
#     opt['dataroot_gt'] = 'tests/data/ffhq_gt.lmdb'
#     opt['io_backend'] = dict(type='lmdb')
#
#     dataset = FFHQDegradationDataset(opt)
#     assert dataset.io_backend_opt['type'] == 'lmdb'  # io backend
#     assert len(dataset) == 1  # whether to read correct meta info
#     assert dataset.kernel_list == ['iso', 'aniso']  # correct initialization the degradation configurations
#     assert dataset.color_jitter_prob == 0
#
#     # test __getitem__
#     result = dataset.__getitem__(0)
#     # check returned keys
#     expected_keys = ['gt', 'lq', 'gt_path']
#     assert set(expected_keys).issubset(set(result.keys()))
#     # check shape and contents
#     assert result['gt'].shape == (3, 512, 512)
#     assert result['lq'].shape == (3, 512, 512)
#     assert result['gt_path'] == '00000000'
#
#     # ------------------ test with crop_components -------------------- #
#     opt['crop_components'] = True
#     opt['component_path'] = 'tests/data/test_eye_mouth_landmarks.pth'
#     opt['eye_enlarge_ratio'] = 1.4
#     opt['gt_gray'] = True
#     opt['io_backend'] = dict(type='lmdb')
#
#     dataset = FFHQDegradationDataset(opt)
#     assert dataset.crop_components is True
#
#     # test __getitem__
#     result = dataset.__getitem__(0)
#     # check returned keys
#     expected_keys = ['gt', 'lq', 'gt_path', 'loc_left_eye', 'loc_right_eye', 'loc_mouth']
#     assert set(expected_keys).issubset(set(result.keys()))
#     # check shape and contents
#     assert result['gt'].shape == (3, 512, 512)
#     assert result['lq'].shape == (3, 512, 512)
#     assert result['gt_path'] == '00000000'
#     assert result['loc_left_eye'].shape == (4, )
#     assert result['loc_right_eye'].shape == (4, )
#     assert result['loc_mouth'].shape == (4, )
#
#     # ------------------ lmdb backend should have paths ends with lmdb -------------------- #
#     with pytest.raises(ValueError):
#         opt['dataroot_gt'] = 'tests/data/gt'
#         opt['io_backend'] = dict(type='lmdb')
#         dataset = FFHQDegradationDataset(opt)
#
test_ffhq_degradation_dataset()