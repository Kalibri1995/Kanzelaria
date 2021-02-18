def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('bin', '/bin')
    config.add_route('shops', '/shops')
    config.add_route('order', '/order')
