from django.db import models

class SurveyResponse(models.Model):
    professor_name = models.CharField(max_length=100)
    question_1 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você sente que a carga de trabalho afeta negativamente sua saúde mental?"
    )
    question_2 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você acredita que recebe apoio adequado da administração escolar para lidar com o estresse?"
    )
    question_3 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você tem acesso a recursos ou programas de bem-estar oferecidos pela sua instituição?"
    )
    question_4 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você sente que seu ambiente de trabalho é seguro e acolhedor?"
    )
    question_6 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você já precisou tirar licença médica por motivos relacionados ao estresse ou à saúde mental?"
    )
    question_7 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você consegue falar abertamente sobre suas preocupações de saúde mental com seus colegas ou superiores?"
    )
    question_8 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você acredita que sua escola oferece suporte suficiente para melhorar a saúde mental dos professores?"
    )
    question_9 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você já participou de alguma palestra ou workshop sobre gestão do estresse ou saúde mental?"
    )
    question_10 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você se sente valorizado(a) e reconhecido(a) em seu ambiente de trabalho?"
    )
    question_11 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você tem tempo suficiente para cuidar da sua saúde mental e física fora do trabalho?"
    )
    question_12 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você acha que as pausas e intervalos durante o expediente são suficientes para recarregar as energias?"
    )
    question_13 = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        verbose_name="Você já considerou mudar de profissão devido ao impacto do trabalho na sua saúde mental?"
    )
    predicted_class = models.IntegerField(
        choices=[(1, 'SIM'), (0, 'NÃO')],
        null=True,
        blank=True,
        verbose_name="Classe prevista pelo modelo"
    )

    def __str__(self):
        return self.professor_name
