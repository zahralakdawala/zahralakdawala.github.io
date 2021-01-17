#%%
import os
import json
import glob
#%%


LINK = '/teaching'

PATH = "../static/teaching"
BASE = 'base.txt'
JSON = 'info.json'
COURSES = os.path.join(PATH,'*')

# VIDEO_LINK = lambda x: os.path.join(x,'video.txt')
# OTHER_LINK = lambda x: os.path.join(x,'other.txt')
BASE_LINK = lambda x: os.path.join(x,BASE)
JSON_LINK = lambda x: os.path.join(x,JSON)

def fix_path(x):
    return x.replace('\\','/')


def get_modules(x):
    modules = glob.glob(os.path.join(x,'*'))
    
    return list(filter(lambda x: os.path.isdir(x),modules))

PDF = ['pdf']
PYTHON = ['py']

def type_setter(path):
    ext = os.path.basename(path).split('.')[-1]
    if ext in PDF:
        return 'PDF'
    elif ext in PYTHON:
        return 'PYTHON'
    return 'OTHER'

def module_setup(y):
    files = glob.glob(os.path.join(y,'*'))
    data = {}
    data['title'] = os.path.basename(y)
    data['content'] = []
    for x in files:
        temp = {}
        temp['title'] = os.path.basename(x).split('.')[0].replace('_',' ')
        temp['link'] = fix_path(x.replace(PATH,LINK))
        temp['type'] = type_setter(x)
        data['content'] += [temp]
    return data

for x in glob.glob(COURSES):
    # files = glob.glob(os.path.join(x,'*'))
    data = {}
    info = open(BASE_LINK(x),'r').read().split('\n')
    info = list(filter(lambda x: x[0] != "#",info))
    data['head'] = info[0]
    data['link'] = info[1]
    data['title'] = info[2]
    data['fullTitle'] = info[3]
    data['text'] = info[4]
    data['img'] = info[5]
    data['carousel'] = info[6:]
    
    modules = get_modules(x)
    
    data['modules'] = [module_setup(module) for module in modules]
    
    with open(JSON_LINK(x), 'w') as outfile:
        json.dump(data, outfile, indent=4)
    # y = open(,'w').write(json.dumps(data))

#%%