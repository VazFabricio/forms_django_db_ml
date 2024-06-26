# Generated by Django 4.2.13 on 2024-06-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("monitoramento_professores", "0003_remove_surveyresponse_question_5_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyresponse",
            name="predicted_class",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "SIM"), (0, "NÃO")],
                null=True,
                verbose_name="Classe prevista pelo modelo",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_1",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você sente que a carga de trabalho afeta negativamente sua saúde mental?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_10",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você se sente valorizado(a) e reconhecido(a) em seu ambiente de trabalho?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_11",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você tem tempo suficiente para cuidar da sua saúde mental e física fora do trabalho?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_12",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você acha que as pausas e intervalos durante o expediente são suficientes para recarregar as energias?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_13",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você já considerou mudar de profissão devido ao impacto do trabalho na sua saúde mental?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_2",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você acredita que recebe apoio adequado da administração escolar para lidar com o estresse?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_3",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você tem acesso a recursos ou programas de bem-estar oferecidos pela sua instituição?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_4",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você sente que seu ambiente de trabalho é seguro e acolhedor?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_6",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você já precisou tirar licença médica por motivos relacionados ao estresse ou à saúde mental?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_7",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você consegue falar abertamente sobre suas preocupações de saúde mental com seus colegas ou superiores?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_8",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você acredita que sua escola oferece suporte suficiente para melhorar a saúde mental dos professores?",
            ),
        ),
        migrations.AlterField(
            model_name="surveyresponse",
            name="question_9",
            field=models.IntegerField(
                choices=[(1, "SIM"), (0, "NÃO")],
                verbose_name="Você já participou de alguma palestra ou workshop sobre gestão do estresse ou saúde mental?",
            ),
        ),
    ]
