# 9-12 Multiple Modules
import privileges_module

admin = privileges_module.Admin('John', 'Smith', 'admin', 'Canada')
admin.privileges.show_privileges()