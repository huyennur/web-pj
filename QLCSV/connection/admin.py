from django.contrib import admin
from connection.models import Group, Group_comment, Group_post
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class GroupManagement(admin.ModelAdmin):
    fields = ['group_name', 'group_infor', 'group_area']


class GroupPostManagement(admin.ModelAdmin):
    fields = ['groupID', 'g_post_user', 'g_post_title',
              'g_post_content', 'g_post_date', 'g_post_comment', 'g_post_image']


class GroupCmtManagement(admin.ModelAdmin):
    fields = ['g_postID', 'g_cmt_user',
              'g_cmt_content', 'g_cmt_date', 'g_cmt_image']


class GroupResources(resources.ModelResource):
    class Meta:
        model = Group


class GroupCmtResources(resources.ModelResource):
    class Meta:
        model = Group_comment


class GroupPostResources(resources.ModelResource):
    class Meta:
        model = Group_post


class GroupAdmin(ImportExportModelAdmin):
    list_display = ('group_name', 'group_infor', 'group_area')
    resources_class = GroupResources


class GroupPostAdmin(ImportExportModelAdmin):
    list_display = ('groupID', 'g_post_user', 'g_post_title',
                    'g_post_content', 'g_post_date', 'g_post_comment', 'g_post_image')
    resources_class = GroupCmtResources


class GroupCmtAdmin(ImportExportModelAdmin):
    list_display = ('g_postID', 'g_cmt_user', 'g_cmt_content',
                    'g_cmt_date', 'g_cmt_image')
    resources_class = GroupPostResources


admin.site.register(Group, GroupAdmin)
admin.site.register(Group_comment, GroupCmtAdmin)
admin.site.register(Group_post, GroupPostAdmin)
