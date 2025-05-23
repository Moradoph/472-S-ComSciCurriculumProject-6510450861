# Generated by Django 5.1.5 on 2025-02-20 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_creditdetail_form_subcategorydetails_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='curriculum_id',
            new_name='curriculum_fk',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='subcategory_id',
            new_name='subcategory_fk',
        ),
        migrations.RenameField(
            model_name='creditdetail',
            old_name='verification_result_id',
            new_name='verification_result_fk',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='course_id',
            new_name='course_fk',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user_id',
            new_name='user_fk',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='user_id',
            new_name='user_fk',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_id',
            new_name='category_fk',
        ),
        migrations.RenameField(
            model_name='subcategorydetails',
            old_name='credit_details_id',
            new_name='credit_details_fk',
        ),
        migrations.RenameField(
            model_name='subcategorydetails',
            old_name='subcateory_id',
            new_name='subcateory_fk',
        ),
        migrations.RenameField(
            model_name='verificationresult',
            old_name='form_id',
            new_name='form_fk',
        ),
    ]
