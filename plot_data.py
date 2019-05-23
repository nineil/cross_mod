# Nils Murrugarra
# University of Pittsburgh

import scipy.io as sio
from skimage import io, img_as_float
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText
import pandas as pd

# functions
def textonly(ax, txt, fontsize = 8, loc = 2, *args, **kwargs):
    at = AnchoredText(txt, prop=dict(size=fontsize), frameon=True, loc=loc)
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)
    return at

if __name__ == "__main__":
    # parameters
    dataset = 'coco' # coco | ads

    # main
    shared_folder = './'
    in_df = shared_folder + 'data_' + dataset + '.csv'
    df = pd.DataFrame.from_csv(in_df)

    # example visualization [input]
    ix_row = 20 #0 | 20
    user_id = df['task_id'][ix_row]
    image = df['image'][ix_row]
    ad_msg = df['ad_msg'][ix_row]
    per_ks = ['reserved', 'trusting', 'lazy', 'relaxed', 'artistic', 'outgoing', 'fault', 'job', 'nervous', 'imagination']
    per = df['personality'][ix_row] # personality data # 1: disagree strongly, 2: disagree a little, 3: neither agree or disagree, 4: agree a little, 5: agree strongly
    per_vals = per[1:-1].split(' ')
    per_str = map(lambda x, y: x + ': ' + y +'\n', per_ks, per_vals)
    per_str = reduce(lambda x, y: x +y, per_str)
    per_str = per_str[:-1]

    sp = image.split('/')
    prefix = sp[0]
    suffix = '/'.join(sp[1:])

    bv_name = shared_folder + '/bv/' + prefix + '/' + suffix.replace('.jpg', '') + '_' + str(user_id) + '.mat' # image + user_id
    im_name = shared_folder + '/ims/' + image
    mask = sio.loadmat(bv_name)['hm']

    im = io.imread(im_name)
    im = img_as_float(im)

    assert im.shape[:2] == mask.shape

    # visualization
    plt.imshow(im, interpolation='nearest')
    plt.imshow(mask, cmap='jet', interpolation='nearest', alpha=.6)
    plt.title( ad_msg )
    textonly(plt.gca(), per_str, loc = 2)
    plt.axis('off')
    plt.show()
