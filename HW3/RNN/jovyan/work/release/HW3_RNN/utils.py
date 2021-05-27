import os
import torch
WEIGHT_PATH = './weights'
if not os.path.isdir(WEIGHT_PATH): os.makedirs(WEIGHT_PATH)

def save_model(model, key, dirpath = WEIGHT_PATH, device=None):
    if device is None: device = next(model.parameters()).device
    dirpath = os.path.join(dirpath, device.type)
    if not os.path.isdir(dirpath): os.makedirs(dirpath)
    fpath = os.path.join(dirpath, '%s.pth'%key)
    torch.save(model.state_dict(), fpath)
    return True

def load_model(model, key, dirpath = WEIGHT_PATH, device=None):
    if device is None: device = next(model.parameters()).device
    dirpath = os.path.join(dirpath, device.type)
    fpath = os.path.join(dirpath, '%s.pth'%key)
    assert os.path.isfile(fpath)
    model.load_state_dict(torch.load(fpath))
    return model

