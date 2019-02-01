from django.contrib.auth.models import User

from user.models import ApplicationUser

ruben = ApplicationUser()
ruben.username = 'rbuhl'
ruben.password = 'ruben'
ruben.email = 'ruben.buhl@gmx.de'
ruben.name = 'Ruben Buhl'

robin = ApplicationUser()
robin.username = 'rlange'
robin.password = 'robin'
robin.email = 'robin.lange@gmx.de'
robin.name = 'Robin Lange'

ruben.save()
robin.save()

ApplicationUser.objects.create_superuser('admin', 'admin@example.com', 'orangeorange')
