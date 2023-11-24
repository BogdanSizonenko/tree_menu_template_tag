from django.db import models


#Модель(таблица) названий меню
class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True , blank=False, null=False, verbose_name='Menu Title')

    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    def __str__(self):
        return self.title
    

#Модель(таблица) опций меню с привязкой к определнному меню и возможностью древовидного меню
class Option(models.Model):
    title = models.CharField(max_length=255, verbose_name='Option Title')
    menu = models.ForeignKey(Menu, blank=False, null=False, related_name='menu_options', on_delete=models.CASCADE)
    parent_option = models.ForeignKey('self', blank=True, null=True, related_name='child_option', on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Menu option'
        verbose_name_plural = 'Menus options'
        
    def __str__(self) -> str:
        return self.title 