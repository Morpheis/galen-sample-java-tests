@@ import header.spec

==============================================================

banner           id          header__fullspan--top

==============================================================


@ Banner | desktop
--------------------------------------------------------------

header-banner:
    below: header-breadcrumbs ~ 0px
    width: 1170px
    height: 600px


@ ^ | tablet
--------------------------------------------------------------

header-banner:
    below: header-breadcrumbs ~ 0px
    width: 970px
    height: 300px


@ ^ | mobile
--------------------------------------------------------------

header-banner:
    absent