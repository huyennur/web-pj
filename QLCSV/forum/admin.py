from django.contrib import admin
from forum.models import Post, Comment
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PostManagement(admin.ModelAdmin):
    fields = ['post_user', 'post_title', 'post_content',
              'post_date', 'post_like', 'post_comment', 'post_image']


class CommentManagement(admin.ModelAdmin):
    fields = ['postID', 'cmt_user', 'cmt_content',
              'cmt_like', 'cmt_date', 'cmt_image']


class PostResources(resources.ModelResource):
    class Meta:
        model = Post


class CommentResources(resources.ModelResource):
    class Meta:
        model = Comment


class PostAdmin(ImportExportModelAdmin):
    list_display = ('post_user', 'post_title', 'post_content',
                    'post_date', 'post_like', 'post_comment', 'post_image')
    resources_class = PostResources


class CommentAdmin(ImportExportModelAdmin):
    list_display = ('postID', 'cmt_user', 'cmt_content',
                    'cmt_like', 'cmt_date', 'cmt_image')
    resources_class = CommentResources


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
