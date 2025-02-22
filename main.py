import deblender as db


data_shapes = {
    'blended': (80, 80, 3),
    'x': (80, 80, 3),
    'y': (80, 80, 3)
}

rrdn_params = {'C':2, 'D':3, 'G':64, 'G0':64, 'T':10}

sampler = db.utils.DataSampler(
    train_path='data/train',
    valid_path='data/valid',
    test_path='data/test',
    data_shapes=data_shapes,
    batch_size=8
)

generator = db.rdn_models.Generator(params=rrdn_params, patch_size=80)
discriminator = db.rdn_models.Discriminator(patch_size=80)
vgg = db.models.VGG19()

logdir = 'logs/logdir'
ckptdir = 'logs/ckptdir'

gan = db.graph.Graph(
    generator=generator,
    discriminator=discriminator,
    vgg=vgg,
    sampler=sampler,
    logdir=logdir,
    ckptdir=ckptdir
)

gan.train()

#gan.image_evaluate(savedir='data/predictions')
#psnr, ssim = gan.metric_evaluate()
#print(psnr, ssim)
