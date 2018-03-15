## Training on 25000 training examples

```
Training model for 40 epochs
training set: 25000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 2
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 7.7316069711064435
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 25000  epoch done in 148.67 seconds    new loss: 0.5418818513739028    new acc: 0.737
epoch 2, learning rate 0.8333   instance 25000  epoch done in 154.42 seconds    new loss: 0.49080955878730514   new acc: 0.763
epoch 3, learning rate 0.7143   instance 25000  epoch done in 156.62 seconds    new loss: 0.4755353271518528    new acc: 0.772
epoch 4, learning rate 0.6250   instance 25000  epoch done in 160.19 seconds    new loss: 0.4554313591821647    new acc: 0.788
epoch 5, learning rate 0.5556   instance 25000  epoch done in 159.09 seconds    new loss: 0.418740148386143     new acc: 0.81
epoch 6, learning rate 0.5000   instance 25000  epoch done in 160.10 seconds    new loss: 0.46447566382885963   new acc: 0.78
epoch 7, learning rate 0.4545   instance 25000  epoch done in 162.68 seconds    new loss: 0.38685181815659775   new acc: 0.838
epoch 8, learning rate 0.4167   instance 25000  epoch done in 129.73 seconds    new loss: 0.4019474716326485    new acc: 0.817
epoch 9, learning rate 0.3846   instance 25000  epoch done in 130.37 seconds    new loss: 0.38272139546368256   new acc: 0.825
epoch 10, learning rate 0.3571  instance 25000  epoch done in 129.13 seconds    new loss: 0.3851074162539322    new acc: 0.834
epoch 11, learning rate 0.3333  instance 25000  epoch done in 128.77 seconds    new loss: 0.4068615930828701    new acc: 0.81
epoch 12, learning rate 0.3125  instance 25000  epoch done in 149.15 seconds    new loss: 0.34761987744926337   new acc: 0.856
epoch 13, learning rate 0.2941  instance 25000  epoch done in 164.53 seconds    new loss: 0.3453079066995954    new acc: 0.868
epoch 14, learning rate 0.2778  instance 25000  epoch done in 166.75 seconds    new loss: 0.4072470059865989    new acc: 0.815
epoch 15, learning rate 0.2632  instance 25000  epoch done in 169.72 seconds    new loss: 0.3402010243368482    new acc: 0.86
epoch 16, learning rate 0.2500  instance 25000  epoch done in 167.86 seconds    new loss: 0.33291755702938924   new acc: 0.867
epoch 17, learning rate 0.2381  instance 25000  epoch done in 173.28 seconds    new loss: 0.33017072636474326   new acc: 0.866
epoch 18, learning rate 0.2273  instance 25000  epoch done in 170.16 seconds    new loss: 0.3512046902242683    new acc: 0.852
epoch 19, learning rate 0.2174  instance 25000  epoch done in 173.10 seconds    new loss: 0.3643282334130099    new acc: 0.846
epoch 20, learning rate 0.2083  instance 25000  epoch done in 171.25 seconds    new loss: 0.35277530451053146   new acc: 0.849
epoch 21, learning rate 0.2000  instance 25000  epoch done in 169.34 seconds    new loss: 0.3198506069797505    new acc: 0.871
epoch 22, learning rate 0.1923  instance 25000  epoch done in 171.30 seconds    new loss: 0.3656069745816016    new acc: 0.841
epoch 23, learning rate 0.1852  instance 25000  epoch done in 170.54 seconds    new loss: 0.31239458195226827   new acc: 0.871
epoch 24, learning rate 0.1786  instance 25000  epoch done in 168.65 seconds    new loss: 0.3137180464722123    new acc: 0.869
epoch 25, learning rate 0.1724  instance 25000  epoch done in 156.96 seconds    new loss: 0.36038774008659563   new acc: 0.849
epoch 26, learning rate 0.1667  instance 25000  epoch done in 131.40 seconds    new loss: 0.31150277383867503   new acc: 0.867
epoch 27, learning rate 0.1613  instance 25000  epoch done in 130.17 seconds    new loss: 0.3170033742845269    new acc: 0.865
epoch 28, learning rate 0.1562  instance 25000  epoch done in 129.66 seconds    new loss: 0.33876773288105505   new acc: 0.85
epoch 29, learning rate 0.1515  instance 25000  epoch done in 130.51 seconds    new loss: 0.3231052658225939    new acc: 0.858
epoch 30, learning rate 0.1471  instance 25000  epoch done in 129.34 seconds    new loss: 0.30082302444353437   new acc: 0.875
epoch 31, learning rate 0.1429  instance 25000  epoch done in 129.05 seconds    new loss: 0.3207057255917465    new acc: 0.865
epoch 32, learning rate 0.1389  instance 25000  epoch done in 128.79 seconds    new loss: 0.3392887685996241    new acc: 0.855
epoch 33, learning rate 0.1351  instance 25000  epoch done in 128.90 seconds    new loss: 0.31829327821684356   new acc: 0.864
epoch 34, learning rate 0.1316  instance 25000  epoch done in 130.75 seconds    new loss: 0.29888305492505873   new acc: 0.867
epoch 35, learning rate 0.1282  instance 25000  epoch done in 129.24 seconds    new loss: 0.3239374941187558    new acc: 0.865
epoch 36, learning rate 0.1250  instance 25000  epoch done in 130.68 seconds    new loss: 0.3068685596863685    new acc: 0.871
epoch 37, learning rate 0.1220  instance 25000  epoch done in 129.73 seconds    new loss: 0.2954781402155974    new acc: 0.881
epoch 38, learning rate 0.1190  instance 25000  epoch done in 151.79 seconds    new loss: 0.30105038639528076   new acc: 0.871
epoch 39, learning rate 0.1163  instance 25000  epoch done in 147.14 seconds    new loss: 0.2950271859667167    new acc: 0.873
epoch 40, learning rate 0.1136  instance 25000  epoch done in 145.83 seconds    new loss: 0.2892617383981172    new acc: 0.876

training finished after reaching maximum of 40 epochs
best observed loss was 0.2892617383981172, acc 0.876, at epoch 40
setting U, V, W to matrices from best epoch
Unadjusted: 1.335
Adjusted for missing vocab: 1.051
```

## Hyperparameter tuning

```
Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 0
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 7.076089209069355
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 8.82 seconds      new loss: 1.7901902446433569    new acc: 0.341
epoch 2, learning rate 0.8333   instance 1000   epoch done in 8.89 seconds      new loss: 1.105303321161985     new acc: 0.659
epoch 3, learning rate 0.7143   instance 1000   epoch done in 9.24 seconds      new loss: 0.757335701558983     new acc: 0.659
epoch 4, learning rate 0.6250   instance 1000   epoch done in 9.60 seconds      new loss: 0.6432481615780701    new acc: 0.668
epoch 5, learning rate 0.5556   instance 1000   epoch done in 9.85 seconds      new loss: 0.6664101262113339    new acc: 0.662
epoch 6, learning rate 0.5000   instance 1000   epoch done in 9.96 seconds      new loss: 0.6594821258583551    new acc: 0.666
epoch 7, learning rate 0.4545   instance 1000   epoch done in 9.94 seconds      new loss: 0.6610380328892105    new acc: 0.666
epoch 8, learning rate 0.4167   instance 1000   epoch done in 9.91 seconds      new loss: 0.693720138968464     new acc: 0.664
epoch 9, learning rate 0.3846   instance 1000   epoch done in 9.75 seconds      new loss: 0.6406839443296367    new acc: 0.668
epoch 10, learning rate 0.3571  instance 1000   epoch done in 9.86 seconds      new loss: 0.6367280088541291    new acc: 0.668

training finished after reaching maximum of 10 epochs
best observed loss was 0.6367280088541291, acc 0.668, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.890
Adjusted for missing vocab: 1.554

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 0
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 7.3218875892295285
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 9.79 seconds      new loss: 0.7471987462313316    new acc: 0.613
epoch 2, learning rate 0.4167   instance 1000   epoch done in 9.85 seconds      new loss: 0.6931645258548758    new acc: 0.659
epoch 3, learning rate 0.3571   instance 1000   epoch done in 9.76 seconds      new loss: 0.6772843477169623    new acc: 0.667
epoch 4, learning rate 0.3125   instance 1000   epoch done in 9.76 seconds      new loss: 0.6753858066086539    new acc: 0.659
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.25 seconds     new loss: 0.685800580955341     new acc: 0.659
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.37 seconds     new loss: 0.646839175642286     new acc: 0.669
epoch 7, learning rate 0.2273   instance 1000   epoch done in 9.96 seconds      new loss: 0.6557502356648718    new acc: 0.662
epoch 8, learning rate 0.2083   instance 1000   epoch done in 9.88 seconds      new loss: 0.6458670063136416    new acc: 0.668
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.73 seconds     new loss: 0.6436182334138305    new acc: 0.668
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.05 seconds     new loss: 0.6371738036235379    new acc: 0.668

training finished after reaching maximum of 10 epochs
best observed loss was 0.6371738036235379, acc 0.668, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.891
Adjusted for missing vocab: 1.555

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 0
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 7.820062307579435
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.04 seconds     new loss: 4.605545674644398     new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 9.97 seconds      new loss: 1.8169753742267334    new acc: 0.659
epoch 3, learning rate 0.0714   instance 1000   epoch done in 9.91 seconds      new loss: 1.103998838307185     new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 9.91 seconds      new loss: 0.8424816553799371    new acc: 0.659
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.01 seconds     new loss: 0.7607785375900097    new acc: 0.659
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.04 seconds     new loss: 0.7275799711088276    new acc: 0.659
epoch 7, learning rate 0.0455   instance 1000   epoch done in 10.11 seconds     new loss: 0.7109406654336604    new acc: 0.659
epoch 8, learning rate 0.0417   instance 1000   epoch done in 10.24 seconds     new loss: 0.6997407058032598    new acc: 0.659
epoch 9, learning rate 0.0385   instance 1000   epoch done in 10.50 seconds     new loss: 0.6913511958520757    new acc: 0.659
epoch 10, learning rate 0.0357  instance 1000   epoch done in 10.16 seconds     new loss: 0.6845041314769044    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6845041314769044, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.983
Adjusted for missing vocab: 1.640

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 0
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 7.29576314265761
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 10.00 seconds     new loss: 5.685140337827739     new acc: 0.658
epoch 2, learning rate 0.0417   instance 1000   epoch done in 10.02 seconds     new loss: 4.156139760563328     new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 10.19 seconds     new loss: 3.073550096743551     new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 10.07 seconds     new loss: 2.5558249224052623    new acc: 0.659
epoch 5, learning rate 0.0278   instance 1000   epoch done in 10.00 seconds     new loss: 2.269030300454879     new acc: 0.659
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.09 seconds     new loss: 2.0360668493561627    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 10.14 seconds     new loss: 1.8354608704920645    new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 10.19 seconds     new loss: 1.6570448781418774    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 10.14 seconds     new loss: 1.4976320779609864    new acc: 0.659
epoch 10, learning rate 0.0179  instance 1000   epoch done in 10.11 seconds     new loss: 1.3540927320373102    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 1.3540927320373102, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 3.873
Adjusted for missing vocab: 3.486

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 2
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 7.22022048701824
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 10.56 seconds     new loss: 1.7442524899942091    new acc: 0.659
epoch 2, learning rate 0.8333   instance 1000   epoch done in 10.31 seconds     new loss: 0.7705945542061913    new acc: 0.37
epoch 3, learning rate 0.7143   instance 1000   epoch done in 10.32 seconds     new loss: 0.690541599829947     new acc: 0.617
epoch 4, learning rate 0.6250   instance 1000   epoch done in 10.31 seconds     new loss: 0.7724081251214666    new acc: 0.348
epoch 5, learning rate 0.5556   instance 1000   epoch done in 10.39 seconds     new loss: 0.6272898834695989    new acc: 0.669
epoch 6, learning rate 0.5000   instance 1000   epoch done in 10.45 seconds     new loss: 0.6230494833892086    new acc: 0.668
epoch 7, learning rate 0.4545   instance 1000   epoch done in 10.28 seconds     new loss: 0.6203047899361285    new acc: 0.669
epoch 8, learning rate 0.4167   instance 1000   epoch done in 10.57 seconds     new loss: 0.6246958943069376    new acc: 0.668
epoch 9, learning rate 0.3846   instance 1000   epoch done in 10.32 seconds     new loss: 0.6083896045314187    new acc: 0.669
epoch 10, learning rate 0.3571  instance 1000   epoch done in 10.44 seconds     new loss: 0.6498769681149059    new acc: 0.668

training finished after reaching maximum of 10 epochs
best observed loss was 0.6083896045314187, acc 0.669, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.837
Adjusted for missing vocab: 1.506

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 2
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 8.562545084140059
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 10.42 seconds     new loss: 0.7180761949252066    new acc: 0.659
epoch 2, learning rate 0.4167   instance 1000   epoch done in 10.36 seconds     new loss: 0.703076239733315     new acc: 0.659
epoch 3, learning rate 0.3571   instance 1000   epoch done in 10.35 seconds     new loss: 0.6492520309770028    new acc: 0.659
epoch 4, learning rate 0.3125   instance 1000   epoch done in 10.97 seconds     new loss: 0.6436335136278618    new acc: 0.659
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.35 seconds     new loss: 0.6636275515329062    new acc: 0.67
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.32 seconds     new loss: 0.6353264771777073    new acc: 0.659
epoch 7, learning rate 0.2273   instance 1000   epoch done in 10.40 seconds     new loss: 0.6325962684498354    new acc: 0.665
epoch 8, learning rate 0.2083   instance 1000   epoch done in 10.40 seconds     new loss: 0.6323573046471992    new acc: 0.659
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.41 seconds     new loss: 0.6399708025291398    new acc: 0.659
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.44 seconds     new loss: 0.6253648478984624    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6253648478984624, acc 0.669, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.869
Adjusted for missing vocab: 1.535

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 2
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 8.367116693002474
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.32 seconds     new loss: 4.670203224269652     new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 10.39 seconds     new loss: 2.303587949191232     new acc: 0.659
epoch 3, learning rate 0.0714   instance 1000   epoch done in 10.37 seconds     new loss: 1.5780571419173919    new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 10.32 seconds     new loss: 1.0577800100885633    new acc: 0.659
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.37 seconds     new loss: 0.8474838744881684    new acc: 0.659
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.45 seconds     new loss: 0.775600788838327     new acc: 0.659
epoch 7, learning rate 0.0455   instance 1000   epoch done in 10.33 seconds     new loss: 0.7430505947112966    new acc: 0.659
epoch 8, learning rate 0.0417   instance 1000   epoch done in 10.33 seconds     new loss: 0.7248420494516971    new acc: 0.659
epoch 9, learning rate 0.0385   instance 1000   epoch done in 10.39 seconds     new loss: 0.7110952220195856    new acc: 0.659
epoch 10, learning rate 0.0357  instance 1000   epoch done in 10.57 seconds     new loss: 0.7024832645172531    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.7024832645172531, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.019
Adjusted for missing vocab: 1.674

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 2
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 7.826820190954413
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 10.21 seconds     new loss: 5.824412251301592     new acc: 0.565
epoch 2, learning rate 0.0417   instance 1000   epoch done in 10.12 seconds     new loss: 3.9794408162294532    new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 10.21 seconds     new loss: 2.747288108777021     new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 10.22 seconds     new loss: 2.2013543793784396    new acc: 0.659
epoch 5, learning rate 0.0278   instance 1000   epoch done in 10.28 seconds     new loss: 1.8873542396269476    new acc: 0.659
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.31 seconds     new loss: 1.6259826574696834    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 10.20 seconds     new loss: 1.4100878233069256    new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 10.22 seconds     new loss: 1.2306649600862327    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 11.02 seconds     new loss: 1.0908421680326026    new acc: 0.66
epoch 10, learning rate 0.0179  instance 1000   epoch done in 10.30 seconds     new loss: 0.992804324489947     new acc: 0.661

training finished after reaching maximum of 10 epochs
best observed loss was 0.992804324489947, acc 0.661, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.699
Adjusted for missing vocab: 2.321

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 8.995221757352061
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 10.52 seconds     new loss: 0.8969123387061945    new acc: 0.341
epoch 2, learning rate 0.8333   instance 1000   epoch done in 10.41 seconds     new loss: 0.7337391436020257    new acc: 0.663
epoch 3, learning rate 0.7143   instance 1000   epoch done in 10.31 seconds     new loss: 0.6652039812613072    new acc: 0.666
epoch 4, learning rate 0.6250   instance 1000   epoch done in 10.73 seconds     new loss: 0.6450460443484743    new acc: 0.669
epoch 5, learning rate 0.5556   instance 1000   epoch done in 10.43 seconds     new loss: 0.64639024833016      new acc: 0.669
epoch 6, learning rate 0.5000   instance 1000   epoch done in 10.45 seconds     new loss: 0.6332767727527593    new acc: 0.669
epoch 7, learning rate 0.4545   instance 1000   epoch done in 10.41 seconds     new loss: 0.6383257769741704    new acc: 0.669
epoch 8, learning rate 0.4167   instance 1000   epoch done in 10.50 seconds     new loss: 0.6502411837060817    new acc: 0.669
epoch 9, learning rate 0.3846   instance 1000   epoch done in 10.40 seconds     new loss: 0.6287832482646907    new acc: 0.669
epoch 10, learning rate 0.3571  instance 1000   epoch done in 10.47 seconds     new loss: 0.6284514701111727    new acc: 0.667

training finished after reaching maximum of 10 epochs
best observed loss was 0.6284514701111727, acc 0.667, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.875
Adjusted for missing vocab: 1.540

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 8.527042566954531
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 10.49 seconds     new loss: 1.0012972854872653    new acc: 0.341
epoch 2, learning rate 0.4167   instance 1000   epoch done in 10.35 seconds     new loss: 0.668354041351332     new acc: 0.665
epoch 3, learning rate 0.3571   instance 1000   epoch done in 10.37 seconds     new loss: 0.6747910232149211    new acc: 0.662
epoch 4, learning rate 0.3125   instance 1000   epoch done in 10.43 seconds     new loss: 0.6610512255434503    new acc: 0.662
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.40 seconds     new loss: 0.6598886977179071    new acc: 0.662
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.47 seconds     new loss: 0.6528332032026056    new acc: 0.662
epoch 7, learning rate 0.2273   instance 1000   epoch done in 10.58 seconds     new loss: 0.6574579058737411    new acc: 0.662
epoch 8, learning rate 0.2083   instance 1000   epoch done in 10.50 seconds     new loss: 0.6445872147802014    new acc: 0.662
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.84 seconds     new loss: 0.6374506879121008    new acc: 0.664
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.40 seconds     new loss: 0.6337201696970431    new acc: 0.664

training finished after reaching maximum of 10 epochs
best observed loss was 0.6337201696970431, acc 0.664, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.885
Adjusted for missing vocab: 1.549

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 8.126832411068598
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.38 seconds     new loss: 4.400947373277396     new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 10.33 seconds     new loss: 2.0780980882316573    new acc: 0.659
epoch 3, learning rate 0.0714   instance 1000   epoch done in 10.38 seconds     new loss: 1.3187669311627574    new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 10.35 seconds     new loss: 0.91801714411223      new acc: 0.659
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.35 seconds     new loss: 0.7931728265909112    new acc: 0.659
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.37 seconds     new loss: 0.747280402433329     new acc: 0.659
epoch 7, learning rate 0.0455   instance 1000   epoch done in 10.41 seconds     new loss: 0.7250366206642429    new acc: 0.659
epoch 8, learning rate 0.0417   instance 1000   epoch done in 10.51 seconds     new loss: 0.7099263151734826    new acc: 0.659
epoch 9, learning rate 0.0385   instance 1000   epoch done in 10.38 seconds     new loss: 0.6997811336248181    new acc: 0.659
epoch 10, learning rate 0.0357  instance 1000   epoch done in 10.59 seconds     new loss: 0.6919833778832275    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6919833778832275, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.998
Adjusted for missing vocab: 1.654

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 7.556074762826846
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 10.29 seconds     new loss: 5.570125564084656     new acc: 0.005
epoch 2, learning rate 0.0417   instance 1000   epoch done in 10.53 seconds     new loss: 3.538227966238065     new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 14.85 seconds     new loss: 2.032464499077123     new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 10.34 seconds     new loss: 1.4544291448531907    new acc: 0.659
epoch 5, learning rate 0.0278   instance 1000   epoch done in 10.37 seconds     new loss: 1.1788157200776477    new acc: 0.659
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.39 seconds     new loss: 1.0079865662097747    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 10.60 seconds     new loss: 0.9083580543957982    new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 10.46 seconds     new loss: 0.8478721158732788    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 10.56 seconds     new loss: 0.8100814540155323    new acc: 0.659
epoch 10, learning rate 0.0179  instance 1000   epoch done in 10.59 seconds     new loss: 0.7842888638913921    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.7842888638913921, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.191
Adjusted for missing vocab: 1.835

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 0
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 7.706361008845344
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 10.35 seconds     new loss: 2.0572164089660925    new acc: 0.341
epoch 2, learning rate 0.8333   instance 1000   epoch done in 10.36 seconds     new loss: 0.7652621140171082    new acc: 0.659
epoch 3, learning rate 0.7143   instance 1000   epoch done in 11.54 seconds     new loss: 0.6670157914109154    new acc: 0.665
epoch 4, learning rate 0.6250   instance 1000   epoch done in 10.43 seconds     new loss: 0.6853143591732246    new acc: 0.599
epoch 5, learning rate 0.5556   instance 1000   epoch done in 10.50 seconds     new loss: 0.6270424233587232    new acc: 0.669
epoch 6, learning rate 0.5000   instance 1000   epoch done in 10.43 seconds     new loss: 0.6242558400426452    new acc: 0.69
epoch 7, learning rate 0.4545   instance 1000   epoch done in 10.63 seconds     new loss: 0.6593027464950326    new acc: 0.667
epoch 8, learning rate 0.4167   instance 1000   epoch done in 10.48 seconds     new loss: 0.610399664467464     new acc: 0.686
epoch 9, learning rate 0.3846   instance 1000   epoch done in 11.07 seconds     new loss: 0.6087066964882598    new acc: 0.673
epoch 10, learning rate 0.3571  instance 1000   epoch done in 10.56 seconds     new loss: 0.6125451552260395    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6087066964882598, acc 0.673, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.838
Adjusted for missing vocab: 1.506

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 0
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 9.151486965479526
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 10.46 seconds     new loss: 0.6973593746080834    new acc: 0.659
epoch 2, learning rate 0.4167   instance 1000   epoch done in 10.36 seconds     new loss: 0.6649768992058569    new acc: 0.668
epoch 3, learning rate 0.3571   instance 1000   epoch done in 10.43 seconds     new loss: 0.8434089095641993    new acc: 0.341
epoch 4, learning rate 0.3125   instance 1000   epoch done in 10.44 seconds     new loss: 0.6408580648542899    new acc: 0.669
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.95 seconds     new loss: 0.6333672517312334    new acc: 0.669
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.52 seconds     new loss: 0.6313329029952743    new acc: 0.669
epoch 7, learning rate 0.2273   instance 1000   epoch done in 10.47 seconds     new loss: 0.6356436568320118    new acc: 0.669
epoch 8, learning rate 0.2083   instance 1000   epoch done in 10.91 seconds     new loss: 0.6576080148079139    new acc: 0.669
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.55 seconds     new loss: 0.6408942676021562    new acc: 0.669
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.58 seconds     new loss: 0.62554721878032      new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.62554721878032, acc 0.669, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.869
Adjusted for missing vocab: 1.535

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 0
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 9.115761843972281
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.35 seconds     new loss: 1.8148108745074965    new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 10.31 seconds     new loss: 0.81641384373946      new acc: 0.669
epoch 3, learning rate 0.0714   instance 1000   epoch done in 10.34 seconds     new loss: 0.7247588797173588    new acc: 0.667
epoch 4, learning rate 0.0625   instance 1000   epoch done in 10.44 seconds     new loss: 0.6968616585390042    new acc: 0.67
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.47 seconds     new loss: 0.6821237239980633    new acc: 0.67
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.63 seconds     new loss: 0.6750576118498366    new acc: 0.67
epoch 7, learning rate 0.0455   instance 1000   epoch done in 9.47 seconds      new loss: 0.668531256278246     new acc: 0.669
epoch 8, learning rate 0.0417   instance 1000   epoch done in 9.52 seconds      new loss: 0.6664122510663854    new acc: 0.67
epoch 9, learning rate 0.0385   instance 1000   epoch done in 9.48 seconds      new loss: 0.6619521106325367    new acc: 0.669
epoch 10, learning rate 0.0357  instance 1000   epoch done in 9.56 seconds      new loss: 0.6608553653301054    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6608553653301054, acc 0.669, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.936
Adjusted for missing vocab: 1.597

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 0
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 7.351750085213686
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 9.41 seconds      new loss: 3.418957215508295     new acc: 0.657
epoch 2, learning rate 0.0417   instance 1000   epoch done in 9.39 seconds      new loss: 1.5964858188874769    new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 9.37 seconds      new loss: 1.0693615706117736    new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 9.47 seconds      new loss: 0.8727090137629467    new acc: 0.659
epoch 5, learning rate 0.0278   instance 1000   epoch done in 9.35 seconds      new loss: 0.7982749907536648    new acc: 0.659
epoch 6, learning rate 0.0250   instance 1000   epoch done in 9.52 seconds      new loss: 0.7619301172983644    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 9.34 seconds      new loss: 0.7396646035617394    new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 9.46 seconds      new loss: 0.7261772749048758    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 9.41 seconds      new loss: 0.7155688152222989    new acc: 0.659
epoch 10, learning rate 0.0179  instance 1000   epoch done in 9.34 seconds      new loss: 0.707634211752534     new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.707634211752534, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.029
Adjusted for missing vocab: 1.683

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 2
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 8.88334301316343
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 9.78 seconds      new loss: 3.62973459903822      new acc: 0.659
epoch 2, learning rate 0.8333   instance 1000   epoch done in 9.86 seconds      new loss: 1.244926608805284     new acc: 0.341
epoch 3, learning rate 0.7143   instance 1000   epoch done in 9.72 seconds      new loss: 0.6799034989807332    new acc: 0.637
epoch 4, learning rate 0.6250   instance 1000   epoch done in 9.70 seconds      new loss: 0.663987860875389     new acc: 0.652
epoch 5, learning rate 0.5556   instance 1000   epoch done in 9.67 seconds      new loss: 0.6211905089764387    new acc: 0.669
epoch 6, learning rate 0.5000   instance 1000   epoch done in 9.70 seconds      new loss: 0.6133510610662538    new acc: 0.672
epoch 7, learning rate 0.4545   instance 1000   epoch done in 9.76 seconds      new loss: 0.6066572505088468    new acc: 0.672
epoch 8, learning rate 0.4167   instance 1000   epoch done in 9.72 seconds      new loss: 0.602316997139449     new acc: 0.676
epoch 9, learning rate 0.3846   instance 1000   epoch done in 9.83 seconds      new loss: 0.6338739802680716    new acc: 0.669
epoch 10, learning rate 0.3571  instance 1000   epoch done in 9.70 seconds      new loss: 0.6075747507050014    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.602316997139449, acc 0.676, at epoch 8
setting U, V, W to matrices from best epoch
Unadjusted: 1.826
Adjusted for missing vocab: 1.495

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 2
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 9.625384000723113
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 9.82 seconds      new loss: 0.8831875579230161    new acc: 0.342
epoch 2, learning rate 0.4167   instance 1000   epoch done in 9.73 seconds      new loss: 0.9952305446163044    new acc: 0.659
epoch 3, learning rate 0.3571   instance 1000   epoch done in 9.81 seconds      new loss: 0.7713458569840508    new acc: 0.349
epoch 4, learning rate 0.3125   instance 1000   epoch done in 9.84 seconds      new loss: 0.7774175751587978    new acc: 0.35
epoch 5, learning rate 0.2778   instance 1000   epoch done in 9.93 seconds      new loss: 0.6349353390972943    new acc: 0.669
epoch 6, learning rate 0.2500   instance 1000   epoch done in 9.79 seconds      new loss: 0.6915660098902119    new acc: 0.666
epoch 7, learning rate 0.2273   instance 1000   epoch done in 9.64 seconds      new loss: 0.6320199478905774    new acc: 0.679
epoch 8, learning rate 0.2083   instance 1000   epoch done in 9.75 seconds      new loss: 0.6555417939254784    new acc: 0.669
epoch 9, learning rate 0.1923   instance 1000   epoch done in 9.74 seconds      new loss: 0.659564730372881     new acc: 0.669
epoch 10, learning rate 0.1786  instance 1000   epoch done in 9.79 seconds      new loss: 0.6203870524703743    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6203870524703743, acc 0.669, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.860
Adjusted for missing vocab: 1.526

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 2
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 8.226965204646522
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 9.81 seconds      new loss: 2.891067125840705     new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 9.71 seconds      new loss: 1.3505867873620745    new acc: 0.659
epoch 3, learning rate 0.0714   instance 1000   epoch done in 9.75 seconds      new loss: 0.8128539263018405    new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 9.67 seconds      new loss: 0.7321708252664675    new acc: 0.659
epoch 5, learning rate 0.0556   instance 1000   epoch done in 9.78 seconds      new loss: 0.7021517679484416    new acc: 0.659
epoch 6, learning rate 0.0500   instance 1000   epoch done in 9.79 seconds      new loss: 0.687337604096694     new acc: 0.659
epoch 7, learning rate 0.0455   instance 1000   epoch done in 9.98 seconds      new loss: 0.6778312762680483    new acc: 0.659
epoch 8, learning rate 0.0417   instance 1000   epoch done in 9.81 seconds      new loss: 0.6728043430999107    new acc: 0.659
epoch 9, learning rate 0.0385   instance 1000   epoch done in 9.81 seconds      new loss: 0.6669003526697448    new acc: 0.659
epoch 10, learning rate 0.0357  instance 1000   epoch done in 9.83 seconds      new loss: 0.6627295484845073    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6627295484845073, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.940
Adjusted for missing vocab: 1.600

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 2
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 9.297153916654482
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 9.71 seconds      new loss: 4.406670049178058     new acc: 0.076
epoch 2, learning rate 0.0417   instance 1000   epoch done in 9.68 seconds      new loss: 1.592368821157225     new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 9.67 seconds      new loss: 1.0078010497416188    new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 9.88 seconds      new loss: 0.8329437333875223    new acc: 0.663
epoch 5, learning rate 0.0278   instance 1000   epoch done in 9.79 seconds      new loss: 0.7735748881057873    new acc: 0.663
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.02 seconds     new loss: 0.7416506482682202    new acc: 0.664
epoch 7, learning rate 0.0227   instance 1000   epoch done in 9.77 seconds      new loss: 0.7247874286281643    new acc: 0.664
epoch 8, learning rate 0.0208   instance 1000   epoch done in 9.75 seconds      new loss: 0.7108414153562121    new acc: 0.667
epoch 9, learning rate 0.0192   instance 1000   epoch done in 9.72 seconds      new loss: 0.7026330487834515    new acc: 0.667
epoch 10, learning rate 0.0179  instance 1000   epoch done in 9.73 seconds      new loss: 0.6947120957092409    new acc: 0.666

training finished after reaching maximum of 10 epochs
best observed loss was 0.6947120957092409, acc 0.666, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.003
Adjusted for missing vocab: 1.659

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 5
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 8.533362350084632
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 10.08 seconds     new loss: 1.213025132175086     new acc: 0.341
epoch 2, learning rate 0.8333   instance 1000   epoch done in 10.11 seconds     new loss: 0.806308765346044     new acc: 0.473
epoch 3, learning rate 0.7143   instance 1000   epoch done in 10.06 seconds     new loss: 0.7057989792993039    new acc: 0.669
epoch 4, learning rate 0.6250   instance 1000   epoch done in 10.04 seconds     new loss: 0.6622550096336949    new acc: 0.673
epoch 5, learning rate 0.5556   instance 1000   epoch done in 10.08 seconds     new loss: 0.6788081261844229    new acc: 0.609
epoch 6, learning rate 0.5000   instance 1000   epoch done in 10.07 seconds     new loss: 0.6171996523389244    new acc: 0.669
epoch 7, learning rate 0.4545   instance 1000   epoch done in 10.01 seconds     new loss: 0.6172897169690724    new acc: 0.669
epoch 8, learning rate 0.4167   instance 1000   epoch done in 10.06 seconds     new loss: 0.5974393336328123    new acc: 0.692
epoch 9, learning rate 0.3846   instance 1000   epoch done in 10.10 seconds     new loss: 0.6808723296677436    new acc: 0.669
epoch 10, learning rate 0.3571  instance 1000   epoch done in 10.04 seconds     new loss: 0.5965789947474626    new acc: 0.682

training finished after reaching maximum of 10 epochs
best observed loss was 0.5965789947474626, acc 0.682, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.816
Adjusted for missing vocab: 1.486

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 5
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 7.819247834747457
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 9.99 seconds      new loss: 2.84120646698668      new acc: 0.659
epoch 2, learning rate 0.4167   instance 1000   epoch done in 10.08 seconds     new loss: 1.0871698560551295    new acc: 0.341
epoch 3, learning rate 0.3571   instance 1000   epoch done in 10.21 seconds     new loss: 0.7078529343424251    new acc: 0.663
epoch 4, learning rate 0.3125   instance 1000   epoch done in 10.17 seconds     new loss: 0.6903980046563052    new acc: 0.666
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.08 seconds     new loss: 0.6234964319341835    new acc: 0.669
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.04 seconds     new loss: 0.6303074141875495    new acc: 0.669
epoch 7, learning rate 0.2273   instance 1000   epoch done in 10.17 seconds     new loss: 0.6225991678714453    new acc: 0.697
epoch 8, learning rate 0.2083   instance 1000   epoch done in 10.10 seconds     new loss: 0.6176284511203038    new acc: 0.697
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.05 seconds     new loss: 0.608423587633982     new acc: 0.67
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.08 seconds     new loss: 0.6073692388435881    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6073692388435881, acc 0.669, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.836
Adjusted for missing vocab: 1.504

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 5
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 9.372341731924617
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.37 seconds     new loss: 1.5416903718765023    new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 10.01 seconds     new loss: 0.7969020815988446    new acc: 0.656
epoch 3, learning rate 0.0714   instance 1000   epoch done in 10.13 seconds     new loss: 0.7238785001054525    new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 10.09 seconds     new loss: 0.7000513528282803    new acc: 0.659
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.04 seconds     new loss: 0.6878095292795108    new acc: 0.659
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.12 seconds     new loss: 0.679969256657444     new acc: 0.659
epoch 7, learning rate 0.0455   instance 1000   epoch done in 9.98 seconds      new loss: 0.6755391576602665    new acc: 0.659
epoch 8, learning rate 0.0417   instance 1000   epoch done in 10.07 seconds     new loss: 0.6708925959730444    new acc: 0.659
epoch 9, learning rate 0.0385   instance 1000   epoch done in 10.10 seconds     new loss: 0.6676520951654409    new acc: 0.659
epoch 10, learning rate 0.0357  instance 1000   epoch done in 10.02 seconds     new loss: 0.6695996923013283    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6676520951654409, acc 0.659, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.950
Adjusted for missing vocab: 1.609

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 50
Steps for back propagation: 5
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 9.442829130176293
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 10.16 seconds     new loss: 5.164856235079756     new acc: 0.0
epoch 2, learning rate 0.0417   instance 1000   epoch done in 10.00 seconds     new loss: 1.8755164054075426    new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 10.15 seconds     new loss: 1.1146751494076206    new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 10.04 seconds     new loss: 0.8768328773452227    new acc: 0.659
epoch 5, learning rate 0.0278   instance 1000   epoch done in 10.14 seconds     new loss: 0.7917037882884952    new acc: 0.659
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.01 seconds     new loss: 0.7533064577925066    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 10.09 seconds     new loss: 0.72915446129295      new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 10.00 seconds     new loss: 0.7127573733909842    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 10.08 seconds     new loss: 0.7037535490180716    new acc: 0.659
epoch 10, learning rate 0.0179  instance 1000   epoch done in 10.04 seconds     new loss: 0.6949572946497565    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6949572946497565, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 2.004
Adjusted for missing vocab: 1.660

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 0
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 8.974488807853463
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 10.30 seconds     new loss: 2.4592819409408766    new acc: 0.659
epoch 2, learning rate 0.8333   instance 1000   epoch done in 10.29 seconds     new loss: 0.6735850178687687    new acc: 0.669
epoch 3, learning rate 0.7143   instance 1000   epoch done in 10.32 seconds     new loss: 0.642846342889062     new acc: 0.693
epoch 4, learning rate 0.6250   instance 1000   epoch done in 10.30 seconds     new loss: 0.6980798611638036    new acc: 0.668
epoch 5, learning rate 0.5556   instance 1000   epoch done in 10.29 seconds     new loss: 0.6130125424180569    new acc: 0.703
epoch 6, learning rate 0.5000   instance 1000   epoch done in 10.49 seconds     new loss: 0.7272672172305308    new acc: 0.668
epoch 7, learning rate 0.4545   instance 1000   epoch done in 10.30 seconds     new loss: 0.6394242318050503    new acc: 0.669
epoch 8, learning rate 0.4167   instance 1000   epoch done in 10.23 seconds     new loss: 0.5937240644320233    new acc: 0.711
epoch 9, learning rate 0.3846   instance 1000   epoch done in 10.27 seconds     new loss: 0.5865319962719086    new acc: 0.696
epoch 10, learning rate 0.3571  instance 1000   epoch done in 10.29 seconds     new loss: 0.6236241891305851    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.5865319962719086, acc 0.696, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.798
Adjusted for missing vocab: 1.469

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 0
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 7.914832862980108
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 10.28 seconds     new loss: 1.1879566699905149    new acc: 0.665
epoch 2, learning rate 0.4167   instance 1000   epoch done in 10.80 seconds     new loss: 0.7287491953834023    new acc: 0.489
epoch 3, learning rate 0.3571   instance 1000   epoch done in 10.26 seconds     new loss: 0.6748030885288404    new acc: 0.62
epoch 4, learning rate 0.3125   instance 1000   epoch done in 10.27 seconds     new loss: 0.6879673622739836    new acc: 0.669
epoch 5, learning rate 0.2778   instance 1000   epoch done in 10.39 seconds     new loss: 0.712465619969602     new acc: 0.669
epoch 6, learning rate 0.2500   instance 1000   epoch done in 10.67 seconds     new loss: 0.6696476119135552    new acc: 0.621
epoch 7, learning rate 0.2273   instance 1000   epoch done in 10.27 seconds     new loss: 0.6207248019261767    new acc: 0.672
epoch 8, learning rate 0.2083   instance 1000   epoch done in 10.39 seconds     new loss: 0.6132464685744032    new acc: 0.677
epoch 9, learning rate 0.1923   instance 1000   epoch done in 10.49 seconds     new loss: 0.6144450812818267    new acc: 0.707
epoch 10, learning rate 0.1786  instance 1000   epoch done in 10.32 seconds     new loss: 0.611700678406759     new acc: 0.676

training finished after reaching maximum of 10 epochs
best observed loss was 0.611700678406759, acc 0.676, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.844
Adjusted for missing vocab: 1.511

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 0
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 8.770695504207417
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 10.35 seconds     new loss: 0.8409243087299653    new acc: 0.659
epoch 2, learning rate 0.0833   instance 1000   epoch done in 10.33 seconds     new loss: 0.7109422511682824    new acc: 0.62
epoch 3, learning rate 0.0714   instance 1000   epoch done in 10.30 seconds     new loss: 0.685340860705207     new acc: 0.659
epoch 4, learning rate 0.0625   instance 1000   epoch done in 10.38 seconds     new loss: 0.6565724986083404    new acc: 0.661
epoch 5, learning rate 0.0556   instance 1000   epoch done in 10.37 seconds     new loss: 0.6528372611827937    new acc: 0.673
epoch 6, learning rate 0.0500   instance 1000   epoch done in 10.30 seconds     new loss: 0.644756829803229     new acc: 0.663
epoch 7, learning rate 0.0455   instance 1000   epoch done in 10.27 seconds     new loss: 0.6408307484920001    new acc: 0.664
epoch 8, learning rate 0.0417   instance 1000   epoch done in 10.30 seconds     new loss: 0.6396322469023973    new acc: 0.667
epoch 9, learning rate 0.0385   instance 1000   epoch done in 10.35 seconds     new loss: 0.6370031539910398    new acc: 0.667
epoch 10, learning rate 0.0357  instance 1000   epoch done in 10.38 seconds     new loss: 0.6419123780480078    new acc: 0.665

training finished after reaching maximum of 10 epochs
best observed loss was 0.6370031539910398, acc 0.667, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.891
Adjusted for missing vocab: 1.555

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 0
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 8.876099361754244
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 10.27 seconds     new loss: 2.5972390858988517    new acc: 0.658
epoch 2, learning rate 0.0417   instance 1000   epoch done in 10.33 seconds     new loss: 1.0952447544441033    new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 10.42 seconds     new loss: 0.8058747533346394    new acc: 0.665
epoch 4, learning rate 0.0312   instance 1000   epoch done in 10.31 seconds     new loss: 0.7379351788632554    new acc: 0.651
epoch 5, learning rate 0.0278   instance 1000   epoch done in 10.48 seconds     new loss: 0.7135443093345706    new acc: 0.651
epoch 6, learning rate 0.0250   instance 1000   epoch done in 10.38 seconds     new loss: 0.7041119920436832    new acc: 0.665
epoch 7, learning rate 0.0227   instance 1000   epoch done in 10.42 seconds     new loss: 0.6905884748687295    new acc: 0.66
epoch 8, learning rate 0.0208   instance 1000   epoch done in 10.32 seconds     new loss: 0.6918239822961254    new acc: 0.668
epoch 9, learning rate 0.0192   instance 1000   epoch done in 10.32 seconds     new loss: 0.6787932766969709    new acc: 0.663
epoch 10, learning rate 0.0179  instance 1000   epoch done in 10.32 seconds     new loss: 0.6747500900026341    new acc: 0.664

training finished after reaching maximum of 10 epochs
best observed loss was 0.6747500900026341, acc 0.664, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.964
Adjusted for missing vocab: 1.622

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 2
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 8.734636672647841
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 11.15 seconds     new loss: 0.7910512059410211    new acc: 0.436
epoch 2, learning rate 0.8333   instance 1000   epoch done in 11.06 seconds     new loss: 1.299497770647443     new acc: 0.341
epoch 3, learning rate 0.7143   instance 1000   epoch done in 11.09 seconds     new loss: 0.6821556200423006    new acc: 0.615
epoch 4, learning rate 0.6250   instance 1000   epoch done in 11.05 seconds     new loss: 0.8001683695194587    new acc: 0.392
epoch 5, learning rate 0.5556   instance 1000   epoch done in 11.17 seconds     new loss: 0.6755508949289272    new acc: 0.669
epoch 6, learning rate 0.5000   instance 1000   epoch done in 11.06 seconds     new loss: 0.6776987406888968    new acc: 0.563
epoch 7, learning rate 0.4545   instance 1000   epoch done in 11.04 seconds     new loss: 0.776803298644883     new acc: 0.667
epoch 8, learning rate 0.4167   instance 1000   epoch done in 11.08 seconds     new loss: 0.6469022443819552    new acc: 0.669
epoch 9, learning rate 0.3846   instance 1000   epoch done in 11.06 seconds     new loss: 0.5882979174558226    new acc: 0.706
epoch 10, learning rate 0.3571  instance 1000   epoch done in 11.08 seconds     new loss: 0.585021298785787     new acc: 0.687

training finished after reaching maximum of 10 epochs
best observed loss was 0.585021298785787, acc 0.687, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.795
Adjusted for missing vocab: 1.466

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 2
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 8.212346315568025
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 11.11 seconds     new loss: 0.7663400419067564    new acc: 0.646
epoch 2, learning rate 0.4167   instance 1000   epoch done in 11.19 seconds     new loss: 1.1545973770067859    new acc: 0.659
epoch 3, learning rate 0.3571   instance 1000   epoch done in 11.14 seconds     new loss: 0.7915703311024191    new acc: 0.669
epoch 4, learning rate 0.3125   instance 1000   epoch done in 11.16 seconds     new loss: 0.6360105859943294    new acc: 0.673
epoch 5, learning rate 0.2778   instance 1000   epoch done in 11.16 seconds     new loss: 0.6213598898104484    new acc: 0.669
epoch 6, learning rate 0.2500   instance 1000   epoch done in 11.20 seconds     new loss: 0.6144826633379971    new acc: 0.669
epoch 7, learning rate 0.2273   instance 1000   epoch done in 11.21 seconds     new loss: 0.6628335248648383    new acc: 0.624
epoch 8, learning rate 0.2083   instance 1000   epoch done in 11.15 seconds     new loss: 0.610407917693819     new acc: 0.684
epoch 9, learning rate 0.1923   instance 1000   epoch done in 11.10 seconds     new loss: 0.6104729405969869    new acc: 0.669
epoch 10, learning rate 0.1786  instance 1000   epoch done in 11.03 seconds     new loss: 0.5993239999808997    new acc: 0.67

training finished after reaching maximum of 10 epochs
best observed loss was 0.5993239999808997, acc 0.67, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.821
Adjusted for missing vocab: 1.490

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 2
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 8.356234478692677
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 11.15 seconds     new loss: 0.7983781373035745    new acc: 0.665
epoch 2, learning rate 0.0833   instance 1000   epoch done in 11.59 seconds     new loss: 0.6998356286350169    new acc: 0.666
epoch 3, learning rate 0.0714   instance 1000   epoch done in 11.18 seconds     new loss: 0.6640802315828482    new acc: 0.664
epoch 4, learning rate 0.0625   instance 1000   epoch done in 11.06 seconds     new loss: 0.6531834026051792    new acc: 0.664
epoch 5, learning rate 0.0556   instance 1000   epoch done in 11.37 seconds     new loss: 0.6461561664840969    new acc: 0.666
epoch 6, learning rate 0.0500   instance 1000   epoch done in 11.30 seconds     new loss: 0.6496789893889593    new acc: 0.668
epoch 7, learning rate 0.0455   instance 1000   epoch done in 11.20 seconds     new loss: 0.6433822710250884    new acc: 0.669
epoch 8, learning rate 0.0417   instance 1000   epoch done in 11.17 seconds     new loss: 0.6354798409935478    new acc: 0.671
epoch 9, learning rate 0.0385   instance 1000   epoch done in 11.19 seconds     new loss: 0.6312823153508493    new acc: 0.666
epoch 10, learning rate 0.0357  instance 1000   epoch done in 11.24 seconds     new loss: 0.6341631760540406    new acc: 0.67

training finished after reaching maximum of 10 epochs
best observed loss was 0.6312823153508493, acc 0.666, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.880
Adjusted for missing vocab: 1.545

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 2
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 8.23095444069775
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 11.07 seconds     new loss: 1.6253297024921158    new acc: 0.658
epoch 2, learning rate 0.0417   instance 1000   epoch done in 11.07 seconds     new loss: 0.793984121671233     new acc: 0.665
epoch 3, learning rate 0.0357   instance 1000   epoch done in 11.09 seconds     new loss: 0.7227216910638966    new acc: 0.669
epoch 4, learning rate 0.0312   instance 1000   epoch done in 11.05 seconds     new loss: 0.7090828358761648    new acc: 0.669
epoch 5, learning rate 0.0278   instance 1000   epoch done in 11.11 seconds     new loss: 0.6991660077674293    new acc: 0.669
epoch 6, learning rate 0.0250   instance 1000   epoch done in 11.04 seconds     new loss: 0.6790014748501879    new acc: 0.666
epoch 7, learning rate 0.0227   instance 1000   epoch done in 11.05 seconds     new loss: 0.6731280445867255    new acc: 0.668
epoch 8, learning rate 0.0208   instance 1000   epoch done in 11.05 seconds     new loss: 0.668009963443749     new acc: 0.666
epoch 9, learning rate 0.0192   instance 1000   epoch done in 11.07 seconds     new loss: 0.6666181420247683    new acc: 0.667
epoch 10, learning rate 0.0179  instance 1000   epoch done in 11.07 seconds     new loss: 0.6620692258616427    new acc: 0.666

training finished after reaching maximum of 10 epochs
best observed loss was 0.6620692258616427, acc 0.666, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.939
Adjusted for missing vocab: 1.599

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 5
Initial learning rate set to 1.0, annealing set to 5

calculating initial mean loss on dev set: 9.299932607777059
calculating initial acc on dev set: 0.0

epoch 1, learning rate 1.0000   instance 1000   epoch done in 11.81 seconds     new loss: 1.3821004829528218    new acc: 0.341
epoch 2, learning rate 0.8333   instance 1000   epoch done in 11.78 seconds     new loss: 1.0735655111901166    new acc: 0.341
epoch 3, learning rate 0.7143   instance 1000   epoch done in 11.75 seconds     new loss: 1.0379629686860563    new acc: 0.659
epoch 4, learning rate 0.6250   instance 1000   epoch done in 11.67 seconds     new loss: 0.791926293101853     new acc: 0.668
epoch 5, learning rate 0.5556   instance 1000   epoch done in 11.68 seconds     new loss: 0.9498390337962563    new acc: 0.659
epoch 6, learning rate 0.5000   instance 1000   epoch done in 11.75 seconds     new loss: 0.6441691349945788    new acc: 0.679
epoch 7, learning rate 0.4545   instance 1000   epoch done in 11.75 seconds     new loss: 0.613813521954699     new acc: 0.684
epoch 8, learning rate 0.4167   instance 1000   epoch done in 11.67 seconds     new loss: 0.6296499001695022    new acc: 0.669
epoch 9, learning rate 0.3846   instance 1000   epoch done in 11.80 seconds     new loss: 0.6565278026733169    new acc: 0.669
epoch 10, learning rate 0.3571  instance 1000   epoch done in 11.77 seconds     new loss: 0.5992790823502018    new acc: 0.683

training finished after reaching maximum of 10 epochs
best observed loss was 0.5992790823502018, acc 0.683, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.821
Adjusted for missing vocab: 1.490

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 5
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 8.427647801115258
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 11.70 seconds     new loss: 1.674487823081121     new acc: 0.659
epoch 2, learning rate 0.4167   instance 1000   epoch done in 11.75 seconds     new loss: 1.1866045868250403    new acc: 0.659
epoch 3, learning rate 0.3571   instance 1000   epoch done in 11.79 seconds     new loss: 0.9148088044171041    new acc: 0.342
epoch 4, learning rate 0.3125   instance 1000   epoch done in 11.67 seconds     new loss: 0.8193893802482554    new acc: 0.364
epoch 5, learning rate 0.2778   instance 1000   epoch done in 11.78 seconds     new loss: 1.2485849479856204    new acc: 0.659
epoch 6, learning rate 0.2500   instance 1000   epoch done in 11.75 seconds     new loss: 0.6241407129049326    new acc: 0.669
epoch 7, learning rate 0.2273   instance 1000   epoch done in 11.72 seconds     new loss: 0.6245135938918099    new acc: 0.702
epoch 8, learning rate 0.2083   instance 1000   epoch done in 11.80 seconds     new loss: 0.6768119954981562    new acc: 0.669
epoch 9, learning rate 0.1923   instance 1000   epoch done in 11.71 seconds     new loss: 0.6036089730590991    new acc: 0.671
epoch 10, learning rate 0.1786  instance 1000   epoch done in 11.71 seconds     new loss: 0.6516275929712909    new acc: 0.669

training finished after reaching maximum of 10 epochs
best observed loss was 0.6036089730590991, acc 0.671, at epoch 9
setting U, V, W to matrices from best epoch
Unadjusted: 1.829
Adjusted for missing vocab: 1.497

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 5
Initial learning rate set to 0.1, annealing set to 5

calculating initial mean loss on dev set: 9.76597395428232
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.1000   instance 1000   epoch done in 11.73 seconds     new loss: 0.7938645862490394    new acc: 0.657
epoch 2, learning rate 0.0833   instance 1000   epoch done in 11.71 seconds     new loss: 0.7043356969104473    new acc: 0.664
epoch 3, learning rate 0.0714   instance 1000   epoch done in 11.73 seconds     new loss: 0.6873719126776073    new acc: 0.664
epoch 4, learning rate 0.0625   instance 1000   epoch done in 11.75 seconds     new loss: 0.6811472486098344    new acc: 0.649
epoch 5, learning rate 0.0556   instance 1000   epoch done in 11.78 seconds     new loss: 0.6561530274036033    new acc: 0.667
epoch 6, learning rate 0.0500   instance 1000   epoch done in 11.75 seconds     new loss: 0.652806203396769     new acc: 0.668
epoch 7, learning rate 0.0455   instance 1000   epoch done in 11.72 seconds     new loss: 0.6506280880834315    new acc: 0.668
epoch 8, learning rate 0.0417   instance 1000   epoch done in 11.84 seconds     new loss: 0.6430899881942416    new acc: 0.667
epoch 9, learning rate 0.0385   instance 1000   epoch done in 11.81 seconds     new loss: 0.6416898544336285    new acc: 0.668
epoch 10, learning rate 0.0357  instance 1000   epoch done in 11.68 seconds     new loss: 0.6416896067062127    new acc: 0.668

training finished after reaching maximum of 10 epochs
best observed loss was 0.6416896067062127, acc 0.668, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.900
Adjusted for missing vocab: 1.563

Training model for 10 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 100
Steps for back propagation: 5
Initial learning rate set to 0.05, annealing set to 5

calculating initial mean loss on dev set: 8.213032239210643
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.0500   instance 1000   epoch done in 11.80 seconds     new loss: 2.24580690973858      new acc: 0.659
epoch 2, learning rate 0.0417   instance 1000   epoch done in 11.82 seconds     new loss: 0.9555852242035756    new acc: 0.659
epoch 3, learning rate 0.0357   instance 1000   epoch done in 11.68 seconds     new loss: 0.7917545825251882    new acc: 0.659
epoch 4, learning rate 0.0312   instance 1000   epoch done in 11.69 seconds     new loss: 0.7366068318580435    new acc: 0.658
epoch 5, learning rate 0.0278   instance 1000   epoch done in 12.29 seconds     new loss: 0.7122141779489621    new acc: 0.658
epoch 6, learning rate 0.0250   instance 1000   epoch done in 11.78 seconds     new loss: 0.6999499885828108    new acc: 0.659
epoch 7, learning rate 0.0227   instance 1000   epoch done in 11.73 seconds     new loss: 0.693200145959523     new acc: 0.659
epoch 8, learning rate 0.0208   instance 1000   epoch done in 11.76 seconds     new loss: 0.6868564604938765    new acc: 0.659
epoch 9, learning rate 0.0192   instance 1000   epoch done in 11.81 seconds     new loss: 0.6808027803864132    new acc: 0.659
epoch 10, learning rate 0.0179  instance 1000   epoch done in 11.78 seconds     new loss: 0.6771681109731476    new acc: 0.659

training finished after reaching maximum of 10 epochs
best observed loss was 0.6771681109731476, acc 0.659, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 1.968
Adjusted for missing vocab: 1.627

Finished parameter tuning.

Best params:
hdim = 100
lookback = 2
learning rate = 1.0
```
