class XdbwbRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on lib models to 'xbmcdb'"
        if model._meta.app_label == 'lib':
            return 'xbmcdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on lib models to 'xbmcdb'"
        if model._meta.app_label == 'lib':
            return 'xbmcdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in lib app"
        if obj1._meta.app_label == 'lib' and obj2._meta.app_label == 'lib':
            return True
        # Allow if neither is xbmc app
        elif 'lib' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'xbmcdb' or model._meta.app_label == "lib":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
