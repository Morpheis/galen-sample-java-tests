==============================================================

header-top-bar          xpath       //*[@id='header__top-bar']/parent::*

header-nav              id          .Wr__body
header-logo             id          header__logo
header-menu             id          header__site-nav--desktop
header-search           id          header__search
header-profile-menu     id          header__profile-menu
header-notif-menu       xpath       //button[contains(@class, 'NotifMenu__trigger')]
header-mini-cart        id          header__mini-cart

header-breadcrumbs      xpath       //*[@id='header__breadcrumbs']/child::*[@class='Wr__box']

==============================================================

@ Header | desktop, tablet
--------------------------------------------------------------

header-top-bar
    inside: screen 0px top
    centered horizontally inside: screen 3px
    height: 30px

header-nav
    below: header-top-bar 0px
    height: 70px

header-logo
    inside: header-nav 0px top, 15px left
    height: 95 to 100 % of header-nav/height
    width: 100px
    image: file images\bbcom_logo.png, error 12px

header-menu
    inside: header-nav 0px top
    near: header-logo 20 to 25px right

header-breadcrumbs
    below: header-nav 10px
    height: 20px


@ ^ | desktop
--------------------------------------------------------------

header-top-bar
    width: 1170px

header-nav
    width: 1170px

header-breadcrumbs
    width: 1170px


@ ^ | tablet
--------------------------------------------------------------

header-top-bar
    width: 970px

header-nav
    width: 970px

header-breadcrumbs
    width: 970px


@ ^ | mobile
--------------------------------------------------------------

header-top-bar
    absent

header-nav
    inside: screen 0px top
    height: 66px
    width: < 768px

header-logo
    centered horizontally inside: header-nav
    height: 24px
    width: 38px

header-breadcrumbs
    below: header-nav 10px
    height: 20px

header-nav
    width: < 768px

header-menu
    absent

header-breadcrumbs
    width: < 768px

