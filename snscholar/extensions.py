from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_principal import Principal, Permission, RoleNeed
principal = Principal(use_sessions=True)
pending_permission = Permission(RoleNeed(u'pending'))
new_permission = pending_permission.union(Permission(RoleNeed(u'new')))
dev_permission = Permission(RoleNeed(u'dev'))
admin_permission = dev_permission.union(Permission(RoleNeed(u'admin')))
user_permission = admin_permission.union(Permission(RoleNeed(u'user')))