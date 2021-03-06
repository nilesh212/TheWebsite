from django.contrib import admin
from FirstApp.models import Professional_Resources,Personal_Development_Resources,MyGoal,Challenge1,Challenge2,MyLibrary,Financial_Success_Resources,AddExperience,CommentsandSuggestions,Advice,JobPortal,CompanyOrStartup,ReviewModel,AppreciatedReviewModel
# Register your models here.
admin.site.register(Professional_Resources)
admin.site.register(Personal_Development_Resources)
admin.site.register(MyGoal)
admin.site.register(Challenge1)
admin.site.register(Challenge2)
admin.site.register(Financial_Success_Resources)
admin.site.register(MyLibrary)
admin.site.register(AddExperience)
admin.site.register(Advice)
admin.site.register(JobPortal)

admin.site.register(CompanyOrStartup)
admin.site.register(CommentsandSuggestions)
admin.site.register(AppreciatedReviewModel)


##############################################################################################
#############################       Review Model     #########################################
##############################################################################################
admin.site.register(ReviewModel)