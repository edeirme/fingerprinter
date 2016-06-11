from app import db

class Fingeprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_time = db.Column(db.String(15))
    cookie = db.Column(db.String(256))
    userAgent = db.Column(db.String(80))
    timezone = db.Column(db.String(120))
    screenwidth = db.Column(db.Integer)
    screendepth = db.Column(db.Integer)
    screenheight = db.Column(db.Integer)
    cookieEnabled = db.Column(db.String(10))
    productSub = db.Column(db.String(80))
    vendor = db.Column(db.String(80))
    navigator_platform = db.Column(db.String(150))
    plugins = db.Column(db.String())
    appVersion = db.Column(db.String(300))
    window_name = db.Column(db.String(120))
    languages = db.Column(db.String(300))
    doNotTrack = db.Column(db.String(15))
    flash_Os = db.Column(db.String(50))
    flash_fonts = db.Column(db.String())
    flash_resolution = db.Column(db.String(50))
    flash_language = db.Column(db.String(50))
    addblockEnabled = db.Column(db.String())
    hasLiedLanguages = db.Column(db.String(5))
    hasLiedResolution = db.Column(db.String(5))
    webGlsupported = db.Column(db.String(5))
    canvassupported = db.Column(db.String(5))
    availableWidth = db.Column(db.String(5))
    avaliableHeight = db.Column(db.String(5))
    webglFP = db.Column(db.String())
    canvasFP = db.Column(db.String())
    hasLocalStorage = db.Column(db.String(5))
    hasSessionStorage = db.Column(db.String(5))
    hasLiedOS = db.Column(db.String(5))
    hasLiedBrowser = db.Column(db.String(5))
    transfer_webgl = db.Column(db.String())
    permissions = db.Column(db.String(150))
    maxTouchPoints = db.Column(db.String(4))
    language = db.Column(db.String(20))
    localeStringDate = db.Column(db.String(30))
    msMaxTouchPoints = db.Column(db.String(4))
    hardwareConcurrency = db.Column(db.String(4))
    playbackQuality = db.Column(db.String)
    playerVolume = db.Column(db.String)
    fps = db.Column(db.String)
    social_media_logged_in = db.Column(db.String)
    gpu_fp = db.Column(db.String)
    detected_router = db.Column(db.String)
