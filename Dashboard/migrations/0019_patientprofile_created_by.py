import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0018_questionjour_reponsequestionjour'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='created_by',
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={'role': 'ergo'},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='patients_created',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Créé par',
            ),
        ),
    ]
