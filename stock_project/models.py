# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bonds(models.Model):
    bondid = models.IntegerField(db_column='bondId', primary_key=True)  # Field name made lowercase.
    stocksymbol = models.TextField(db_column='stockSymbol')  # Field name made lowercase.
    numshares = models.IntegerField(db_column='numShares')  # Field name made lowercase.
    purchaseprice = models.FloatField(db_column='purchasePrice')  # Field name made lowercase.
    currentprice = models.FloatField(db_column='currentPrice')  # Field name made lowercase.
    datepurchased = models.TextField(db_column='datePurchased')  # Field name made lowercase.
    investorid = models.IntegerField(db_column='investorID')  # Field name made lowercase.
    coupon = models.FloatField()
    bondyield = models.FloatField(db_column='bondYield')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bonds'


class Investors(models.Model):
    investorid = models.IntegerField(db_column='investorID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='firstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName')  # Field name made lowercase.
    address = models.TextField()
    phonenumber = models.TextField(db_column='phoneNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Investors'


class Stocks(models.Model):
    stockid = models.IntegerField(db_column='stockId', primary_key=True)  # Field name made lowercase.
    stocksymbol = models.TextField(db_column='stockSymbol')  # Field name made lowercase.
    numshares = models.IntegerField(db_column='numShares')  # Field name made lowercase.
    purchaseprice = models.FloatField(db_column='purchasePrice')  # Field name made lowercase.
    currentprice = models.FloatField(db_column='currentPrice')  # Field name made lowercase.
    datepurchased = models.TextField(db_column='datePurchased')  # Field name made lowercase. This field type is a guess.
    investorid = models.IntegerField(db_column='investorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stocks'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
