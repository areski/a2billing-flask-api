import datetime
from app import db
from peewee import *


class CardGroup(db.Model):
    name = CharField()
    description = TextField(null=True)
    users_perms = IntegerField(default=0)
    id_agent = IntegerField(default=0)

    class Meta:
        db_table = 'cc_card_group'


class Card(db.Model):
    # user = ForeignKeyField(User, related_name='tweets')
    creationdate = DateTimeField(default=datetime.datetime.now)
    firstusedate = CharField(null=True)
    expirationdate = CharField(null=True)
    enableexpire = CharField(null=True)
    expiredays = CharField(null=True)
    username = CharField(null=False)
    useralias = CharField()
    uipass = CharField()
    credit = FloatField(default=0.0)
    tariff = CharField()
    id_didgroup = CharField(null=True)
    activated = CharField(choices=(('f', 'False'), ('t', 'True')))
    status = IntegerField(default=1)
    lastname = CharField(default='')
    firstname = CharField(default='')
    address = CharField(default='')
    city = CharField(default='')
    state = CharField(default='')
    country = CharField(default='')
    zipcode = CharField(default='')
    phone = CharField(default='')
    email = CharField(default='')
    fax = CharField(default='')
    # inuse = CharField(null=True)
    simultaccess = IntegerField(default=0)
    currency = CharField(default='USD')
    # lastuse = CharField(null=True)
    # nbused = CharField(null=True)
    typepaid = IntegerField(default=0)
    creditlimit = IntegerField(default=0)
    voipcall = IntegerField(default=0)
    sip_buddy = IntegerField(default=0)
    iax_buddy = IntegerField(default=0)
    language = CharField(default='en')
    redial = CharField(default='')
    runservice = CharField(null=True)
    # nbservice = CharField(null=True)
    # id_campaign = CharField(null=True)
    # num_trials_done = CharField(null=True)
    vat = FloatField(null=False, default=0)
    # servicelastrun = CharField(null=True)
    # Using DecimalField produce an error
    initialbalance = FloatField(default=0.0)
    invoiceday = IntegerField(default=1)
    autorefill = IntegerField(default=0)
    loginkey = CharField(default='')
    mac_addr = CharField(default='00-00-00-00-00-00')
    id_timezone = IntegerField(default=0)
    tag = CharField(default='')
    voicemail_permitted = IntegerField(default=0)
    voicemail_activated = IntegerField(default=0)
    # last_notification = CharField(null=True)
    email_notification = CharField(default='')
    notify_email = IntegerField(default=0)
    credit_notification = IntegerField(default=-1)
    id_group = IntegerField(default=1)
    company_name = CharField(default='')
    company_website = CharField(default='')
    vat_rn = CharField(null=True)
    traffic = BigIntegerField(default=0)
    traffic_target = CharField(default='')
    # Using DecimalField produce an error
    discount = FloatField(default=0.0)
    # restriction = CharField(null=True)
    # id_seria = CharField(null=True)
    # serial = CharField(null=True)
    block = IntegerField(default=0)
    lock_pin = CharField(null=True)
    lock_date = DateTimeField(null=True)
    max_concurrent = IntegerField(default=10)
    # is_published = BooleanField(default=True)

    class Meta:
        db_table = 'cc_card'


class Callerid(db.Model):
    # id = BigIntegerField(primary_key=True)
    # id_cc_card = BigIntegerField()
    id_cc_card = ForeignKeyField(Card, db_column='id_cc_card')
    activated = CharField(default='t')
    cid = CharField(unique=True)

    class Meta:
        db_table = 'cc_callerid'


class Logrefill(db.Model):
    # id = BigIntegerField(primary_key=True)
    # card = ForeignKeyField(Card, db_column='card_id')
    card = BigIntegerField(db_column='card_id', null=True)
    date = DateTimeField(null=True)
    agent = BigIntegerField(db_column='agent_id', null=True)
    credit = DecimalField(default=0.0)
    description = TextField(null=True)
    # refill_type (amount:0, correction:1, extra fee:2,agent refund:3)
    refill_type = IntegerField(default=0)
    added_invoice = IntegerField(default=0)

    class Meta:
        db_table = 'cc_logrefill'


class Logpayment(db.Model):
    card = BigIntegerField(db_column='card_id')
    date = DateTimeField(null=True, default=datetime.datetime.now)
    description = TextField(null=True)
    payment = DecimalField(default=0.0)
    # payment_type (amount:0, correction:1, extra fee:2,agent refund:3)
    payment_type = IntegerField(default=0)
    id_logrefill = BigIntegerField(null=True)
    added_commission = IntegerField(default=0)
    added_refill = IntegerField(default=0)
    agent = BigIntegerField(db_column='agent_id', null=True)

    class Meta:
        db_table = 'cc_logpayment'


class Country(db.Model):
    # id = BigIntegerField(primary_key=True)
    countrycode = CharField()
    countryname = CharField()
    countryprefix = CharField()

    class Meta:
        db_table = 'cc_country'

    def __str__(self):
        return self.countryname


class Did(db.Model):
    # id = BigIntegerField(primary_key=True)
    # id_cc_country = IntegerField()
    # id_cc_didgroup = BigIntegerField()
    id_cc_didgroup = IntegerField(null=False)
    id_cc_country = ForeignKeyField(Country, related_name='country', db_column='id_cc_country')
    activated = IntegerField(null=False)
    did = CharField(unique=True)
    reserved = IntegerField(null=True)
    iduser = BigIntegerField(null=False)
    creationdate = DateTimeField(default=datetime.datetime.now)
    startingdate = DateTimeField()
    expirationdate = DateTimeField()
    aleg_carrier_connect_charge = DecimalField()
    aleg_carrier_connect_charge_offp = DecimalField()
    aleg_carrier_cost_min = DecimalField()
    aleg_carrier_cost_min_offp = DecimalField()
    aleg_carrier_increment = IntegerField()
    aleg_carrier_increment_offp = IntegerField()
    aleg_carrier_initblock = IntegerField()
    aleg_carrier_initblock_offp = IntegerField()
    aleg_retail_connect_charge = DecimalField()
    aleg_retail_connect_charge_offp = DecimalField()
    aleg_retail_cost_min = DecimalField()
    aleg_retail_cost_min_offp = DecimalField()
    aleg_retail_increment = IntegerField()
    aleg_retail_increment_offp = IntegerField()
    aleg_retail_initblock = IntegerField()
    aleg_retail_initblock_offp = IntegerField()
    aleg_timeinterval = TextField(null=True)
    billingtype = IntegerField(null=True)
    connection_charge = DecimalField()
    description = TextField(null=True)
    fixrate = FloatField()
    max_concurrent = IntegerField()
    secondusedreal = IntegerField(null=True)
    selling_rate = DecimalField()

    class Meta:
        db_table = 'cc_did'


class DidDestination(db.Model):
    # id = BigIntegerField(primary_key=True)
    destination = CharField(null=True)
    priority = IntegerField()
    id_cc_card = BigIntegerField()
    id_cc_did = BigIntegerField()
    activated = IntegerField()
    secondusedreal = IntegerField(null=True)
    voip_call = IntegerField(null=True)
    validated = IntegerField(null=True)
    # creationdate = DateTimeField()

    class Meta:
        db_table = 'cc_did_destination'


class Call(db.Model):
    # id = BigIntegerField(primary_key=True)
    sessionid = CharField(default=0)
    uniqueid = CharField(null=False)
    card_id = BigIntegerField(null=False, db_column='card_id')
    nasipaddress = CharField(null=False)
    starttime = DateTimeField(index=True, default=datetime.datetime.now)
    stoptime = CharField(default="0000-00-00 00:00:00")
    buycost = DecimalField(null=True)
    calledstation = CharField(index=True)
    destination = IntegerField(null=True)
    dnid = CharField(null=False)
    id_card_package_offer = IntegerField(null=True)
    id_did = IntegerField(null=True)
    id_ratecard = IntegerField(null=True)
    id_tariffgroup = IntegerField(null=True)
    id_tariffplan = IntegerField(null=True)
    id_trunk = IntegerField(null=True)
    real_sessiontime = IntegerField(null=True)
    sessionbill = FloatField(null=True)
    sessiontime = IntegerField(null=True)
    sipiax = IntegerField(null=True)
    src = CharField()
    terminatecauseid = IntegerField(index=True, null=True)

    class Meta:
        db_table = 'cc_call'


class Charge(db.Model):
    # id = BigIntegerField(primary_key=True)
    amount = FloatField(default=0)
    charged_status = IntegerField(default=0)
    # Values: 1:charge DID setup, 2:Montly charge for DID use, 3:Subscription fee, 4:Extra Charge
    chargetype = IntegerField(null=True, default=4)
    cover_from = DateField(null=True)
    cover_to = DateField(null=True)
    creationdate = DateTimeField(index=True, default=datetime.datetime.now)
    description = TextField(null=True)
    id_cc_card = ForeignKeyField(Card, db_column='id_cc_card')
    id_cc_card_subscription = BigIntegerField(null=True)
    # id_cc_did = BigIntegerField(null=True)
    id_cc_did = ForeignKeyField(Did, db_column='id_cc_did', default=0)
    iduser = IntegerField(default=0)
    invoiced_status = IntegerField(default=0)

    class Meta:
        db_table = 'cc_charge'


#
# Previous Models are currently used
#


class Agent(db.Model):
    active = CharField()
    address = CharField(null=True)
    bank_info = TextField(null=True)
    banner = TextField(null=True)
    city = CharField(null=True)
    com_balance = DecimalField()
    commission = DecimalField()
    company = CharField(null=True)
    country = CharField(null=True)
    credit = DecimalField()
    currency = CharField(null=True)
    datecreation = DateTimeField()
    email = CharField(null=True)
    fax = CharField(null=True)
    firstname = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    id_tariffgroup = IntegerField(null=True)
    language = CharField(null=True)
    lastname = CharField(null=True)
    locale = CharField(null=True)
    location = TextField(null=True)
    login = CharField(unique=True)
    options = IntegerField()
    passwd = CharField(null=True)
    perms = IntegerField(null=True)
    phone = CharField(null=True)
    state = CharField(null=True)
    threshold_remittance = DecimalField()
    vat = DecimalField()
    zipcode = CharField(null=True)

    class Meta:
        db_table = 'cc_agent'


class AgentCommission(db.Model):
    amount = DecimalField()
    commission_percent = DecimalField()
    commission_type = IntegerField()
    date = DateTimeField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    id_agent = IntegerField()
    id_card = BigIntegerField()
    id_payment = BigIntegerField(null=True)

    class Meta:
        db_table = 'cc_agent_commission'


class AgentSignup(db.Model):
    code = CharField(unique=True)
    id = BigIntegerField(primary_key=True)
    id_agent = IntegerField()
    id_group = IntegerField()
    id_tariffgroup = IntegerField()

    class Meta:
        db_table = 'cc_agent_signup'


class AgentTariffgroup(db.Model):
    id_agent = BigIntegerField()
    id_tariffgroup = IntegerField()

    class Meta:
        db_table = 'cc_agent_tariffgroup'
        indexes = (
            (('id_agent', 'id_tariffgroup'), True),
        )
        primary_key = CompositeKey('id_agent', 'id_tariffgroup')


class Alarm(db.Model):
    datecreate = DateTimeField()
    datelastrun = DateTimeField()
    emailreport = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    id_trunk = IntegerField(null=True)
    maxvalue = FloatField()
    minvalue = FloatField()
    name = TextField()
    numberofalarm = IntegerField()
    numberofrun = IntegerField()
    periode = IntegerField()
    status = IntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'cc_alarm'


class AlarmReport(db.Model):
    calculatedvalue = FloatField()
    cc_alarm = BigIntegerField(db_column='cc_alarm_id')
    daterun = DateTimeField()
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'cc_alarm_report'


class AutorefillReport(db.Model):
    daterun = DateTimeField()
    id = BigIntegerField(primary_key=True)
    totalcardperform = IntegerField(null=True)
    totalcredit = DecimalField(null=True)

    class Meta:
        db_table = 'cc_autorefill_report'


class Backup(db.Model):
    creationdate = DateTimeField()
    id = BigIntegerField(primary_key=True)
    name = CharField(unique=True)
    path = CharField()

    class Meta:
        db_table = 'cc_backup'


class BillingCustomer(db.Model):
    date = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_card = BigIntegerField()
    id_invoice = BigIntegerField()
    start_date = DateTimeField(null=True)

    class Meta:
        db_table = 'cc_billing_customer'


class CallArchive(db.Model):
    buycost = DecimalField(null=True)
    calledstation = CharField(index=True)
    card = BigIntegerField(db_column='card_id')
    destination = IntegerField(null=True)
    dnid = CharField()
    id = BigIntegerField(primary_key=True)
    id_card_package_offer = IntegerField(null=True)
    id_did = IntegerField(null=True)
    id_ratecard = IntegerField(null=True)
    id_tariffgroup = IntegerField(null=True)
    id_tariffplan = IntegerField(null=True)
    id_trunk = IntegerField(null=True)
    nasipaddress = CharField()
    real_sessiontime = IntegerField(null=True)
    sessionbill = FloatField(null=True)
    sessionid = CharField()
    sessiontime = IntegerField(null=True)
    sipiax = IntegerField(null=True)
    src = CharField()
    starttime = DateTimeField(index=True)
    stoptime = DateTimeField()
    terminatecauseid = IntegerField(index=True, null=True)
    uniqueid = CharField()

    class Meta:
        db_table = 'cc_call_archive'


class CallbackSpool(db.Model):
    account = CharField(null=True)
    actionid = CharField(null=True)
    agi_result = CharField(null=True)
    application = CharField(null=True)
    async = CharField(null=True)
    callback_time = DateTimeField()
    callerid = CharField(null=True)
    channel = CharField(null=True)
    context = CharField(null=True)
    data = CharField(null=True)
    entry_time = DateTimeField()
    exten = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    id_server = IntegerField(null=True)
    id_server_group = IntegerField(null=True)
    last_attempt_time = DateTimeField()
    manager_result = CharField(null=True)
    num_attempt = IntegerField()
    priority = CharField(null=True)
    server_ip = CharField(null=True)
    status = CharField(null=True)
    timeout = CharField(null=True)
    uniqueid = CharField(null=True, unique=True)
    variable = CharField(null=True)

    class Meta:
        db_table = 'cc_callback_spool'


class CallplanLcr(db.Model):
    buyrate = DecimalField(null=True)
    connectcharge = DecimalField(null=True)
    destination = CharField(null=True)
    dialprefix = CharField(null=True)
    id = IntegerField(null=True)
    id_trunk = IntegerField(null=True)
    idtariffplan = IntegerField(null=True)
    initblock = IntegerField(null=True)
    ratecard = IntegerField(db_column='ratecard_id', null=True)
    rateinitial = DecimalField(null=True)
    startdate = DateTimeField(null=True)
    stopdate = DateTimeField(null=True)
    tariffgroup = IntegerField(db_column='tariffgroup_id', null=True)

    class Meta:
        db_table = 'cc_callplan_lcr'


class Campaign(db.Model):
    creationdate = DateTimeField()
    daily_start_time = TimeField()
    daily_stop_time = TimeField()
    description = TextField(null=True)
    expirationdate = DateTimeField()
    forward_number = CharField(null=True)
    frequency = IntegerField()
    friday = IntegerField()
    id_campaign_config = IntegerField()
    id_card = BigIntegerField()
    id_cid_group = IntegerField()
    monday = IntegerField()
    name = CharField(unique=True)
    nb_callmade = IntegerField(null=True)
    saturday = IntegerField()
    secondusedreal = IntegerField(null=True)
    startingdate = DateTimeField()
    status = IntegerField()
    sunday = IntegerField()
    thursday = IntegerField()
    tuesday = IntegerField()
    wednesday = IntegerField()

    class Meta:
        db_table = 'cc_campaign'


class CampaignConfig(db.Model):
    context = CharField()
    description = TextField(null=True)
    flatrate = DecimalField()
    name = CharField()

    class Meta:
        db_table = 'cc_campaign_config'


class CampaignPhonebook(db.Model):
    id_campaign = IntegerField()
    id_phonebook = IntegerField()

    class Meta:
        db_table = 'cc_campaign_phonebook'
        indexes = (
            (('id_campaign', 'id_phonebook'), True),
        )
        primary_key = CompositeKey('id_campaign', 'id_phonebook')


class CampaignPhonestatus(db.Model):
    id_callback = CharField()
    id_campaign = IntegerField()
    id_phonenumber = BigIntegerField()
    lastuse = DateTimeField()
    status = IntegerField()

    class Meta:
        db_table = 'cc_campaign_phonestatus'
        indexes = (
            (('id_phonenumber', 'id_campaign'), True),
        )
        primary_key = CompositeKey('id_campaign', 'id_phonenumber')


class CampaignconfCardgroup(db.Model):
    id_campaign_config = IntegerField()
    id_card_group = IntegerField()

    class Meta:
        db_table = 'cc_campaignconf_cardgroup'
        indexes = (
            (('id_campaign_config', 'id_card_group'), True),
        )
        primary_key = CompositeKey('id_campaign_config', 'id_card_group')


class CardArchive(db.Model):
    vat_rn = CharField(db_column='VAT_RN', null=True)
    activated = CharField()
    activatedbyuser = CharField()
    address = CharField(null=True)
    autorefill = IntegerField(null=True)
    city = CharField(null=True)
    company_name = CharField(null=True)
    company_website = CharField(null=True)
    country = CharField(null=True)
    creationdate = DateTimeField(index=True)
    credit = DecimalField()
    credit_notification = IntegerField()
    creditlimit = IntegerField(null=True)
    currency = CharField(null=True)
    discount = DecimalField()
    email = CharField(null=True)
    email_notification = CharField(null=True)
    enableexpire = IntegerField(null=True)
    expirationdate = DateTimeField()
    expiredays = IntegerField(null=True)
    fax = CharField(null=True)
    firstname = CharField(null=True)
    firstusedate = DateTimeField()
    iax_buddy = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    id_campaign = IntegerField(null=True)
    id_didgroup = IntegerField(null=True)
    id_group = IntegerField()
    id_timezone = IntegerField(null=True)
    initialbalance = DecimalField()
    inuse = IntegerField(null=True)
    invoiceday = IntegerField(null=True)
    language = CharField(null=True)
    last_notification = DateTimeField(null=True)
    lastname = CharField(null=True)
    lastuse = DateTimeField()
    loginkey = CharField(null=True)
    mac_addr = CharField()
    nbservice = IntegerField(null=True)
    nbused = IntegerField(null=True)
    notify_email = IntegerField()
    num_trials_done = BigIntegerField(null=True)
    phone = CharField(null=True)
    redial = CharField(null=True)
    restriction = IntegerField()
    runservice = IntegerField(null=True)
    servicelastrun = DateTimeField()
    simultaccess = IntegerField(null=True)
    sip_buddy = IntegerField(null=True)
    state = CharField(null=True)
    status = IntegerField(null=True)
    tag = CharField(null=True)
    tariff = IntegerField(null=True)
    traffic = BigIntegerField(null=True)
    traffic_target = TextField(null=True)
    typepaid = IntegerField(null=True)
    uipass = CharField(null=True)
    useralias = CharField()
    username = CharField(index=True)
    vat = FloatField()
    voicemail_activated = IntegerField()
    voicemail_permitted = IntegerField()
    voipcall = IntegerField(null=True)
    zipcode = CharField(null=True)

    class Meta:
        db_table = 'cc_card_archive'


class CardHistory(db.Model):
    datecreated = DateTimeField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField(null=True)

    class Meta:
        db_table = 'cc_card_history'


class CardPackageOffer(db.Model):
    date_consumption = DateTimeField(index=True)
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField(index=True)
    id_cc_package_offer = BigIntegerField(index=True)
    used_secondes = BigIntegerField()

    class Meta:
        db_table = 'cc_card_package_offer'


class CardSeria(db.Model):
    description = TextField(null=True)
    name = CharField()
    value = BigIntegerField()

    class Meta:
        db_table = 'cc_card_seria'


class CardSubscription(db.Model):
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField(null=True)
    id_subscription_fee = IntegerField(null=True)
    last_run = DateTimeField()
    limit_pay_date = DateTimeField()
    next_billing_date = DateTimeField()
    paid_status = IntegerField()
    product = CharField(db_column='product_id', null=True)
    product_name = CharField(null=True)
    startdate = DateTimeField()
    stopdate = DateTimeField()

    class Meta:
        db_table = 'cc_card_subscription'


class CardgroupService(db.Model):
    id_card_group = IntegerField()
    id_service = IntegerField()

    class Meta:
        db_table = 'cc_cardgroup_service'
        indexes = (
            (('id_card_group', 'id_service'), True),
        )
        primary_key = CompositeKey('id_card_group', 'id_service')


class Config(db.Model):
    config_description = CharField(null=True)
    config_group_title = CharField()
    config_key = CharField(null=True)
    config_listvalues = CharField(null=True)
    config_title = CharField(null=True)
    config_value = CharField(null=True)
    config_valuetype = IntegerField()

    class Meta:
        db_table = 'cc_config'


class ConfigGroup(db.Model):
    group_description = CharField()
    group_title = CharField(unique=True)

    class Meta:
        db_table = 'cc_config_group'


class Configuration(db.Model):
    configuration_description = CharField()
    configuration = PrimaryKeyField(db_column='configuration_id')
    configuration_key = CharField()
    configuration_title = CharField()
    configuration_type = IntegerField()
    configuration_value = CharField()
    set_function = CharField(null=True)
    use_function = CharField(null=True)

    class Meta:
        db_table = 'cc_configuration'


class Currencies(db.Model):
    basecurrency = CharField()
    currency = CharField(unique=True)
    lastupdate = DateTimeField()
    name = CharField()
    value = DecimalField()

    class Meta:
        db_table = 'cc_currencies'


class DidUse(db.Model):
    activated = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField(null=True)
    id_did = BigIntegerField()
    month_payed = IntegerField(null=True)
    releasedate = DateTimeField()
    reminded = IntegerField()
    reservationdate = DateTimeField()

    class Meta:
        db_table = 'cc_did_use'


class Didgroup(db.Model):
    creationdate = DateTimeField()
    didgroupname = CharField()
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'cc_didgroup'


class EpaymentLog(db.Model):
    amount = CharField()
    cardid = BigIntegerField()
    cc_expires = CharField(null=True)
    cc_number = CharField(null=True)
    cc_owner = CharField(null=True)
    creationdate = DateTimeField()
    credit_card_type = CharField(null=True)
    currency = CharField(null=True)
    cvv = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    item = BigIntegerField(db_column='item_id', null=True)
    item_type = CharField(null=True)
    paymentmethod = CharField()
    status = IntegerField()
    transaction_detail = TextField(null=True)
    vat = FloatField()

    class Meta:
        db_table = 'cc_epayment_log'


class EpaymentLogAgent(db.Model):
    agent = BigIntegerField(db_column='agent_id')
    amount = CharField()
    cc_expires = CharField(null=True)
    cc_number = CharField(null=True)
    cc_owner = CharField(null=True)
    creationdate = DateTimeField()
    credit_card_type = CharField(null=True)
    currency = CharField(null=True)
    cvv = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    paymentmethod = CharField()
    status = IntegerField()
    transaction_detail = TextField(null=True)
    vat = FloatField()

    class Meta:
        db_table = 'cc_epayment_log_agent'


class IaxBuddies(db.Model):
    defaultip = CharField(db_column='DEFAULTip', null=True)
    accountcode = CharField()
    adsi = CharField()
    allow = CharField()
    amaflags = CharField(null=True)
    auth = CharField()
    callerid = CharField()
    cid_number = CharField()
    codecpriority = CharField()
    context = CharField()
    dbsecret = CharField()
    deny = CharField()
    disallow = CharField()
    encryption = CharField()
    forcejitterbuffer = CharField()
    fullname = CharField()
    host = CharField(index=True)
    id_cc_card = IntegerField()
    inkeys = CharField()
    ipaddr = CharField(index=True)
    jitterbuffer = CharField()
    language = CharField(null=True)
    mask = CharField()
    maxauthreq = CharField()
    maxcallnumbers = CharField()
    maxcallnumbers_nonvalidated = CharField()
    mohinterpret = CharField()
    mohsuggest = CharField()
    name = CharField(unique=True)
    outkey = CharField()
    permit = CharField(null=True)
    port = CharField(index=True)
    qualify = CharField(null=True)
    qualifyfreqnotok = CharField()
    qualifyfreqok = CharField()
    qualifysmoothing = CharField()
    regcontext = CharField()
    regexten = CharField()
    regseconds = IntegerField()
    requirecalltoken = CharField()
    secret = CharField()
    sendani = CharField()
    setvar = CharField()
    sourceaddress = CharField()
    timezone = CharField()
    transfer = CharField()
    trunk = CharField(null=True)
    type = CharField()
    username = CharField()

    class Meta:
        db_table = 'cc_iax_buddies'
        indexes = (
            (('host', 'port'), False),
            (('ipaddr', 'port'), False),
            (('name', 'host'), False),
            (('name', 'ipaddr', 'port'), False),
        )


class Invoice(db.Model):
    date = DateTimeField()
    description = TextField()
    id = BigIntegerField(primary_key=True)
    id_card = BigIntegerField()
    paid_status = IntegerField()
    reference = CharField(null=True, unique=True)
    status = IntegerField()
    title = CharField()

    class Meta:
        db_table = 'cc_invoice'


class InvoiceConf(db.Model):
    key_val = CharField(unique=True)
    value = CharField()

    class Meta:
        db_table = 'cc_invoice_conf'


class InvoiceItem(db.Model):
    vat = DecimalField(db_column='VAT')
    date = DateTimeField()
    description = TextField()
    id = BigIntegerField(primary_key=True)
    id_ext = BigIntegerField(null=True)
    id_invoice = BigIntegerField()
    price = DecimalField()
    type_ext = CharField(null=True)

    class Meta:
        db_table = 'cc_invoice_item'


class InvoicePayment(db.Model):
    id_invoice = BigIntegerField()
    id_payment = BigIntegerField()

    class Meta:
        db_table = 'cc_invoice_payment'
        indexes = (
            (('id_invoice', 'id_payment'), True),
        )
        primary_key = CompositeKey('id_invoice', 'id_payment')


class Iso639(db.Model):
    charset = CharField()
    code = CharField(primary_key=True)
    lname = CharField(null=True)
    name = CharField(unique=True)

    class Meta:
        db_table = 'cc_iso639'


class LogpaymentAgent(db.Model):
    added_refill = IntegerField()
    agent = BigIntegerField(db_column='agent_id')
    date = DateTimeField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    id_logrefill = BigIntegerField(null=True)
    payment = DecimalField()
    payment_type = IntegerField()

    class Meta:
        db_table = 'cc_logpayment_agent'


class LogrefillAgent(db.Model):
    agent = BigIntegerField(db_column='agent_id')
    credit = DecimalField()
    date = DateTimeField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    refill_type = IntegerField()

    class Meta:
        db_table = 'cc_logrefill_agent'


class MessageAgent(db.Model):
    id = BigIntegerField(primary_key=True)
    id_agent = IntegerField()
    logo = IntegerField()
    message = TextField(null=True)
    order_display = IntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'cc_message_agent'


class Monitor(db.Model):
    description = CharField(null=True)
    dial_code = IntegerField(null=True)
    enable = IntegerField()
    id = BigIntegerField(primary_key=True)
    label = CharField()
    query = CharField(null=True)
    query_type = IntegerField()
    result_type = IntegerField()
    text_intro = CharField(null=True)

    class Meta:
        db_table = 'cc_monitor'


class Notification(db.Model):
    date = DateTimeField()
    from_ = BigIntegerField(db_column='from_id', null=True)
    from_type = IntegerField()
    id = BigIntegerField(primary_key=True)
    key_value = CharField(null=True)
    link = BigIntegerField(db_column='link_id', null=True)
    link_type = CharField(null=True)
    priority = IntegerField()

    class Meta:
        db_table = 'cc_notification'


class NotificationAdmin(db.Model):
    id_admin = IntegerField()
    id_notification = BigIntegerField()
    viewed = IntegerField()

    class Meta:
        db_table = 'cc_notification_admin'
        indexes = (
            (('id_notification', 'id_admin'), True),
        )
        primary_key = CompositeKey('id_admin', 'id_notification')


class OutboundCidGroup(db.Model):
    creationdate = DateTimeField()
    group_name = CharField()

    class Meta:
        db_table = 'cc_outbound_cid_group'


class OutboundCidList(db.Model):
    activated = IntegerField()
    cid = CharField(null=True)
    creationdate = DateTimeField()
    outbound_cid_group = IntegerField()

    class Meta:
        db_table = 'cc_outbound_cid_list'


class PackageGroup(db.Model):
    description = TextField(null=True)
    name = CharField()

    class Meta:
        db_table = 'cc_package_group'


class PackageOffer(db.Model):
    billingtype = IntegerField()
    creationdate = DateTimeField()
    freetimetocall = IntegerField()
    id = BigIntegerField(primary_key=True)
    label = CharField()
    packagetype = IntegerField()
    startday = IntegerField()

    class Meta:
        db_table = 'cc_package_offer'


class PackageRate(db.Model):
    package = IntegerField(db_column='package_id')
    rate = IntegerField(db_column='rate_id')

    class Meta:
        db_table = 'cc_package_rate'
        indexes = (
            (('package', 'rate'), True),
        )
        primary_key = CompositeKey('package', 'rate')


class PackgroupPackage(db.Model):
    package = IntegerField(db_column='package_id')
    packagegroup = IntegerField(db_column='packagegroup_id')

    class Meta:
        db_table = 'cc_packgroup_package'
        indexes = (
            (('packagegroup', 'package'), True),
        )
        primary_key = CompositeKey('package', 'packagegroup')


class PaymentMethods(db.Model):
    payment_filename = CharField()
    payment_method = CharField()

    class Meta:
        db_table = 'cc_payment_methods'


class Payments(db.Model):
    cc_expires = CharField(null=True)
    cc_number = CharField(null=True)
    cc_owner = CharField(null=True)
    cc_type = CharField(null=True)
    currency = CharField(null=True)
    currency_value = DecimalField(null=True)
    customers_email_address = CharField()
    customers = BigIntegerField(db_column='customers_id')
    customers_name = CharField()
    date_purchased = DateTimeField(null=True)
    id = BigIntegerField(primary_key=True)
    item = CharField(db_column='item_id', null=True)
    item_name = CharField(null=True)
    item_quantity = IntegerField()
    last_modified = DateTimeField(null=True)
    orders_amount = DecimalField(null=True)
    orders_date_finished = DateTimeField(null=True)
    orders_status = IntegerField()
    payment_method = CharField()

    class Meta:
        db_table = 'cc_payments'


class PaymentsAgent(db.Model):
    agent_email_address = CharField()
    agent = BigIntegerField(db_column='agent_id')
    agent_name = CharField()
    cc_expires = CharField(null=True)
    cc_number = CharField(null=True)
    cc_owner = CharField(null=True)
    cc_type = CharField(null=True)
    currency = CharField(null=True)
    currency_value = DecimalField(null=True)
    date_purchased = DateTimeField(null=True)
    id = BigIntegerField(primary_key=True)
    item = CharField(db_column='item_id', null=True)
    item_name = CharField(null=True)
    item_quantity = IntegerField()
    last_modified = DateTimeField(null=True)
    orders_amount = DecimalField(null=True)
    orders_date_finished = DateTimeField(null=True)
    orders_status = IntegerField()
    payment_method = CharField()

    class Meta:
        db_table = 'cc_payments_agent'


class PaymentsStatus(db.Model):
    status = IntegerField(db_column='status_id')
    status_name = CharField()

    class Meta:
        db_table = 'cc_payments_status'


class Paypal(db.Model):
    address_city = CharField()
    address_country = CharField()
    address_name = CharField()
    address_state = CharField()
    address_status = CharField()
    address_street = CharField()
    address_zip = CharField()
    first_name = CharField(null=True)
    item_name = CharField(null=True)
    item_number = CharField(null=True)
    last_name = CharField(null=True)
    mc_currency = CharField(null=True)
    mc_fee = DecimalField(null=True)
    mc_gross = DecimalField(null=True)
    memo = TextField(null=True)
    payer_business_name = CharField()
    payer_email = CharField(null=True)
    payer = CharField(db_column='payer_id', null=True)
    payer_status = CharField(null=True)
    payment_date = CharField(null=True)
    payment_status = CharField()
    payment_type = CharField(null=True)
    pending_reason = CharField()
    quantity = IntegerField()
    reason_code = CharField()
    tax = DecimalField(null=True)
    txn = CharField(db_column='txn_id', null=True, unique=True)
    txn_type = CharField()

    class Meta:
        db_table = 'cc_paypal'


class Phonebook(db.Model):
    description = TextField(null=True)
    id_card = BigIntegerField()
    name = CharField()

    class Meta:
        db_table = 'cc_phonebook'


class Phonenumber(db.Model):
    amount = IntegerField()
    creationdate = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_phonebook = IntegerField()
    info = TextField(null=True)
    name = CharField(null=True)
    number = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'cc_phonenumber'


class Prefix(db.Model):
    destination = CharField(index=True)
    prefix = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'cc_prefix'


class Provider(db.Model):
    creationdate = DateTimeField()
    description = TextField(null=True)
    provider_name = CharField(unique=True)

    class Meta:
        db_table = 'cc_provider'


class Ratecard(db.Model):
    additional_block_charge = DecimalField()
    additional_block_charge_time = IntegerField()
    additional_grace = IntegerField()
    announce_time_correction = DecimalField()
    billingblock = IntegerField()
    billingblocka = IntegerField()
    billingblockb = IntegerField()
    billingblockc = IntegerField()
    buyrate = DecimalField()
    buyrateincrement = IntegerField()
    buyrateinitblock = IntegerField()
    chargea = DecimalField()
    chargeb = DecimalField()
    chargec = FloatField()
    connectcharge = DecimalField()
    destination = BigIntegerField(null=True)
    dialprefix = CharField(index=True)
    disconnectcharge = DecimalField()
    disconnectcharge_after = IntegerField()
    endtime = IntegerField(null=True)
    id_outbound_cidgroup = IntegerField(null=True)
    id_trunk = IntegerField(null=True)
    idtariffplan = IntegerField(index=True)
    initblock = IntegerField()
    is_merged = IntegerField(null=True)
    minimal_cost = DecimalField()
    musiconhold = CharField()
    rateinitial = DecimalField()
    rounding_calltime = IntegerField()
    rounding_threshold = IntegerField()
    startdate = DateTimeField()
    starttime = IntegerField(null=True)
    stepchargea = DecimalField()
    stepchargeb = DecimalField()
    stepchargec = FloatField()
    stopdate = DateTimeField()
    tag = CharField(null=True)
    timechargea = IntegerField()
    timechargeb = IntegerField()
    timechargec = IntegerField()

    class Meta:
        db_table = 'cc_ratecard'


class Receipt(db.Model):
    date = DateTimeField()
    description = TextField()
    id = BigIntegerField(primary_key=True)
    id_card = BigIntegerField()
    status = IntegerField()
    title = CharField()

    class Meta:
        db_table = 'cc_receipt'


class ReceiptItem(db.Model):
    date = DateTimeField()
    description = TextField()
    id = BigIntegerField(primary_key=True)
    id_ext = BigIntegerField(null=True)
    id_receipt = BigIntegerField()
    price = DecimalField()
    type_ext = CharField(null=True)

    class Meta:
        db_table = 'cc_receipt_item'


class RemittanceRequest(db.Model):
    amount = DecimalField()
    date = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_agent = BigIntegerField()
    status = IntegerField()
    type = IntegerField()

    class Meta:
        db_table = 'cc_remittance_request'


class RestrictedPhonenumber(db.Model):
    id = BigIntegerField(primary_key=True)
    id_card = BigIntegerField()
    number = CharField()

    class Meta:
        db_table = 'cc_restricted_phonenumber'


class ServerGroup(db.Model):
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    name = CharField(null=True)

    class Meta:
        db_table = 'cc_server_group'


class ServerManager(db.Model):
    id = BigIntegerField(primary_key=True)
    id_group = IntegerField(null=True)
    lasttime_used = DateTimeField()
    manager_host = CharField(null=True)
    manager_secret = CharField(null=True)
    manager_username = CharField(null=True)
    server_ip = CharField(null=True)

    class Meta:
        db_table = 'cc_server_manager'


class Service(db.Model):
    amount = FloatField()
    datecreate = DateTimeField()
    datelastrun = DateTimeField()
    daynumber = IntegerField()
    dialplan = IntegerField(null=True)
    emailreport = CharField()
    id = BigIntegerField(primary_key=True)
    maxnumbercycle = IntegerField()
    name = CharField()
    numberofrun = IntegerField()
    operate_mode = IntegerField(null=True)
    period = IntegerField()
    rule = IntegerField()
    status = IntegerField()
    stopmode = IntegerField()
    totalcardperform = IntegerField()
    totalcredit = FloatField()
    use_group = IntegerField(null=True)

    class Meta:
        db_table = 'cc_service'


class ServiceReport(db.Model):
    cc_service = BigIntegerField(db_column='cc_service_id')
    daterun = DateTimeField()
    id = BigIntegerField(primary_key=True)
    totalcardperform = IntegerField(null=True)
    totalcredit = FloatField(null=True)

    class Meta:
        db_table = 'cc_service_report'


class SipBuddies(db.Model):
    defaultip = CharField(db_column='DEFAULTip', null=True)
    accountcode = CharField()
    allow = CharField()
    allowtransfer = CharField()
    amaflags = CharField(null=True)
    auth = CharField()
    autoframing = CharField()
    callbackextension = CharField(null=True)
    callerid = CharField()
    callgroup = CharField(null=True)
    callingpres = CharField()
    cancallforward = CharField(null=True)
    canreinvite = CharField()
    cid_number = CharField()
    context = CharField()
    defaultuser = CharField()
    deny = CharField()
    disallow = CharField()
    dtmfmode = CharField()
    fromdomain = CharField()
    fromuser = CharField()
    fullcontact = CharField()
    host = CharField(index=True)
    id_cc_card = IntegerField()
    incominglimit = CharField()
    insecure = CharField()
    ipaddr = CharField(index=True)
    language = CharField(null=True)
    lastms = CharField(null=True)
    mailbox = CharField()
    mask = CharField()
    maxcallbitrate = CharField()
    md5secret = CharField()
    mohsuggest = CharField()
    musicclass = CharField()
    musiconhold = CharField()
    name = CharField(unique=True)
    nat = CharField(null=True)
    outboundproxy = CharField()
    permit = CharField(null=True)
    pickupgroup = CharField(null=True)
    port = CharField(index=True)
    qualify = CharField(null=True)
    regexten = CharField()
    regseconds = IntegerField()
    regserver = CharField(null=True)
    restrictcid = CharField(null=True)
    rtpholdtimeout = CharField(null=True)
    rtpkeepalive = CharField()
    rtptimeout = CharField(null=True)
    secret = CharField()
    setvar = CharField()
    subscribecontext = CharField()
    subscribemwi = CharField()
    type = CharField()
    useragent = CharField(null=True)
    usereqphone = CharField()
    username = CharField()
    vmexten = CharField()

    class Meta:
        db_table = 'cc_sip_buddies'
        indexes = (
            (('host', 'port'), False),
            (('ipaddr', 'port'), False),
        )


class SipBuddiesEmpty(db.Model):
    defaultip = CharField(db_column='DEFAULTip', null=True)
    accountcode = CharField()
    allow = CharField()
    amaflags = CharField(null=True)
    callerid = CharField()
    callgroup = CharField(null=True)
    cancallforward = CharField(null=True)
    canreinvite = CharField()
    context = CharField()
    deny = CharField()
    disallow = CharField()
    dtmfmode = CharField()
    fromdomain = CharField()
    fromuser = CharField()
    fullcontact = CharField()
    host = CharField()
    id = IntegerField()
    id_cc_card = IntegerField()
    insecure = CharField()
    ipaddr = CharField()
    language = CharField(null=True)
    mailbox = CharField()
    mask = CharField()
    md5secret = CharField()
    musiconhold = CharField()
    name = CharField()
    nat = CharField(null=True)
    permit = CharField(null=True)
    pickupgroup = CharField(null=True)
    port = CharField()
    qualify = CharField(null=True)
    regexten = CharField()
    regseconds = IntegerField()
    restrictcid = CharField(null=True)
    rtpholdtimeout = CharField(null=True)
    rtptimeout = CharField(null=True)
    secret = CharField()
    setvar = CharField()
    type = CharField()
    username = CharField()

    class Meta:
        db_table = 'cc_sip_buddies_empty'


class Speeddial(db.Model):
    creationdate = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField()
    name = CharField()
    phone = CharField()
    speeddial = IntegerField(null=True)

    class Meta:
        db_table = 'cc_speeddial'
        indexes = (
            (('id_cc_card', 'speeddial'), True),
        )


class StatusLog(db.Model):
    id = BigIntegerField(primary_key=True)
    id_cc_card = BigIntegerField()
    status = IntegerField()
    updated_date = DateTimeField()

    class Meta:
        db_table = 'cc_status_log'


class SubscriptionService(db.Model):
    datecreate = DateTimeField()
    datelastrun = DateTimeField()
    emailreport = CharField()
    fee = FloatField()
    id = BigIntegerField(primary_key=True)
    label = CharField()
    numberofrun = IntegerField()
    startdate = DateTimeField()
    status = IntegerField()
    stopdate = DateTimeField()
    totalcardperform = IntegerField()
    totalcredit = FloatField()

    class Meta:
        db_table = 'cc_subscription_service'


class SubscriptionSignup(db.Model):
    description = CharField(null=True)
    enable = IntegerField()
    id = BigIntegerField(primary_key=True)
    id_callplan = BigIntegerField(null=True)
    id_subscription = BigIntegerField(null=True)
    label = CharField()

    class Meta:
        db_table = 'cc_subscription_signup'


class Support(db.Model):
    email = CharField(null=True)
    language = CharField()
    name = CharField()

    class Meta:
        db_table = 'cc_support'


class SupportComponent(db.Model):
    activated = IntegerField()
    id_support = IntegerField()
    name = CharField()
    type_user = IntegerField()

    class Meta:
        db_table = 'cc_support_component'


class SystemLog(db.Model):
    action = TextField()
    agent = IntegerField(null=True)
    creationdate = DateTimeField()
    data = TextField(null=True)
    description = TextField(null=True)
    iduser = IntegerField()
    ipaddress = CharField(null=True)
    loglevel = IntegerField()
    pagename = CharField(null=True)
    tablename = CharField(null=True)

    class Meta:
        db_table = 'cc_system_log'


class Tariffgroup(db.Model):
    creationdate = DateTimeField()
    id_cc_package_offer = BigIntegerField()
    idtariffplan = IntegerField()
    iduser = IntegerField()
    lcrtype = IntegerField()
    removeinterprefix = IntegerField()
    tariffgroupname = CharField()

    class Meta:
        db_table = 'cc_tariffgroup'


class TariffgroupPlan(db.Model):
    idtariffgroup = IntegerField()
    idtariffplan = IntegerField()

    class Meta:
        db_table = 'cc_tariffgroup_plan'
        indexes = (
            (('idtariffgroup', 'idtariffplan'), True),
        )
        primary_key = CompositeKey('idtariffgroup', 'idtariffplan')


class Tariffplan(db.Model):
    calleridprefix = CharField()
    creationdate = DateTimeField()
    description = TextField(null=True)
    dnidprefix = CharField()
    expirationdate = DateTimeField()
    id_trunk = IntegerField(null=True)
    idowner = IntegerField(null=True)
    iduser = IntegerField()
    reftariffplan = IntegerField(null=True)
    secondusedcarrier = IntegerField(null=True)
    secondusedratecard = IntegerField(null=True)
    secondusedreal = IntegerField(null=True)
    startingdate = DateTimeField()
    tariffname = CharField()

    class Meta:
        db_table = 'cc_tariffplan'
        indexes = (
            (('iduser', 'tariffname'), True),
        )


class Templatemail(db.Model):
    fromemail = CharField(null=True)
    fromname = CharField(null=True)
    id_language = CharField()
    mailtype = CharField(null=True)
    messagehtml = CharField(null=True)
    messagetext = CharField(null=True)
    subject = CharField(null=True)

    class Meta:
        db_table = 'cc_templatemail'
        indexes = (
            (('mailtype', 'id_language'), True),
        )


class Ticket(db.Model):
    creationdate = DateTimeField()
    creator = BigIntegerField()
    creator_type = IntegerField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    id_component = IntegerField()
    priority = IntegerField()
    status = IntegerField()
    title = CharField()
    viewed_admin = IntegerField()
    viewed_agent = IntegerField()
    viewed_cust = IntegerField()

    class Meta:
        db_table = 'cc_ticket'


class TicketComment(db.Model):
    creator = BigIntegerField()
    creator_type = IntegerField()
    date = DateTimeField()
    description = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    id_ticket = BigIntegerField()
    viewed_admin = IntegerField()
    viewed_agent = IntegerField()
    viewed_cust = IntegerField()

    class Meta:
        db_table = 'cc_ticket_comment'


class Timezone(db.Model):
    gmtoffset = BigIntegerField()
    gmttime = CharField(null=True)
    gmtzone = CharField(null=True)

    class Meta:
        db_table = 'cc_timezone'


class Trunk(db.Model):
    addparameter = CharField(null=True)
    creationdate = DateTimeField()
    failover_trunk = IntegerField(null=True)
    id_provider = IntegerField(null=True)
    id_trunk = PrimaryKeyField()
    if_max_use = IntegerField(null=True)
    inuse = IntegerField(null=True)
    maxuse = IntegerField(null=True)
    providerip = CharField()
    providertech = CharField()
    removeprefix = CharField(null=True)
    secondusedcarrier = IntegerField(null=True)
    secondusedratecard = IntegerField(null=True)
    secondusedreal = IntegerField(null=True)
    status = IntegerField(null=True)
    trunkcode = CharField(null=True)
    trunkprefix = CharField(null=True)

    class Meta:
        db_table = 'cc_trunk'


class UiAuthen(db.Model):
    city = CharField(null=True)
    confaddcust = IntegerField(null=True)
    country = CharField(null=True)
    datecreation = DateTimeField()
    direction = CharField(null=True)
    email = CharField(null=True)
    fax = CharField(null=True)
    groupid = IntegerField(null=True)
    login = CharField(unique=True)
    name = CharField(null=True)
    perms = IntegerField(null=True)
    phone = CharField(null=True)
    pwd_encoded = CharField()
    state = CharField(null=True)
    userid = BigIntegerField(primary_key=True)
    zipcode = CharField(null=True)

    class Meta:
        db_table = 'cc_ui_authen'


class Version(db.Model):
    version = CharField()

    class Meta:
        db_table = 'cc_version'


class Voucher(db.Model):
    activated = CharField()
    creationdate = DateTimeField()
    credit = FloatField()
    currency = CharField(null=True)
    expirationdate = DateTimeField()
    id = BigIntegerField(primary_key=True)
    tag = CharField(null=True)
    used = IntegerField(null=True)
    usedate = DateTimeField()
    usedcardnumber = CharField(null=True)
    voucher = CharField(unique=True)

    class Meta:
        db_table = 'cc_voucher'


class Cdrs(db.Model):
    call_start_time = DateTimeField()
    cdr = BigIntegerField(db_column='cdr_id', primary_key=True)
    cost = IntegerField()
    created = DateTimeField()
    dst_domain = CharField()
    dst_ousername = CharField()
    dst_username = CharField()
    duration = IntegerField()
    rated = IntegerField()
    sip_call = CharField(db_column='sip_call_id')
    sip_from_tag = CharField()
    sip_to_tag = CharField()
    src_domain = CharField()
    src_ip = CharField()
    src_username = CharField()

    class Meta:
        db_table = 'cdrs'
        indexes = (
            (('sip_call', 'sip_from_tag', 'sip_to_tag'), True),
        )


class CollectionCdrs(db.Model):
    call_start_time = DateTimeField()
    cdr = BigIntegerField(db_column='cdr_id')
    cost = IntegerField()
    dst_domain = CharField()
    dst_ousername = CharField()
    dst_username = CharField()
    duration = IntegerField()
    flag_imported = IntegerField()
    id = BigIntegerField(primary_key=True)
    rated = IntegerField()
    sip_call = CharField(db_column='sip_call_id')
    sip_code = CharField()
    sip_from_tag = CharField()
    sip_reason = CharField()
    sip_to_tag = CharField()
    src_domain = CharField()
    src_ip = CharField()
    src_username = CharField()

    class Meta:
        db_table = 'collection_cdrs'


class MissedCalls(db.Model):
    callid = CharField(index=True)
    cdr = IntegerField(db_column='cdr_id')
    dst_domain = CharField()
    dst_ouser = CharField()
    dst_user = CharField()
    from_tag = CharField()
    method = CharField()
    sip_code = CharField()
    sip_reason = CharField()
    src_domain = CharField()
    src_ip = CharField()
    src_user = CharField()
    time = DateTimeField()
    to_tag = CharField()

    class Meta:
        db_table = 'missed_calls'


class Note(db.Model):
    created = DateTimeField()
    message = TextField()

    class Meta:
        db_table = 'note'


class User(db.Model):
    active = IntegerField()
    admin = IntegerField()
    email = CharField(unique=True)
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'user'
