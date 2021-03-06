# Generated by Django 2.2.7 on 2019-11-25 14:25

from django.db import migrations


def make_initial_data_for_accounts(apps, schema_editor):
    AccountType = apps.get_model('accounting', 'AccountType')
    data = [
        {
            'id': 'asset',
            'name': 'Assets',
            'normal_balance': 'debit'
        },
        {
            'id': 'liabilities',
            'name': 'Liabilities',
            'normal_balance': 'credit'
        },
        {
            'id': 'equity',
            'name': 'Equity',
            'normal_balance': 'credit'
        },
        {
            'id': 'revenue',
            'name': 'Revenues',
            'normal_balance': 'credit'
        },
        {
            'id': 'expenses',
            'name': 'Expenses',
            'normal_balance': 'debit'
        },
    ]
    for d in data:
        if not AccountType.objects.filter(pk=d['id']).exists():
            AccountType.objects.create(**d)


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_initial_data_for_accounts)
    ]
