from modeltranslation.translator import translator, TranslationOptions
from web.models import Project, About


class ProjectTranslationOptions(TranslationOptions):
    fields = ('overview', 'intro', 'goals', 'challenges', 'solutions', 'impact', 'conclusion',)


class AboutTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Project, ProjectTranslationOptions)
translator.register(About, AboutTranslationOptions)
