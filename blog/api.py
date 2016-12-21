from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from blog.models import PostImage, Post


class PostResource(ModelResource):
    body_html = fields.CharField(attribute='body_html', use_in='detail')

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        fields = ['id', 'title', 'body_html']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'put', 'patch']
        authentication = Authentication()
        authorization = DjangoAuthorization()

    def get_object_list(self, request):
        return super(PostResource, self).get_object_list(request).filter(author=request.user)



class ImageResource(ModelResource):
    post = fields.ForeignKey(PostResource, 'post')

    class Meta:
        queryset = PostImage.objects.all()
        resource_name = 'image'
        fields = ['id', 'image']
        list_allowed_methods = ['get', 'post']
        authentication = Authentication()
        authorization = DjangoAuthorization()
        filtering = {
            'post': ALL_WITH_RELATIONS,
        }

    def get_object_list(self, request):
        return super(ImageResource, self).get_object_list(request).filter(owner=request.user)


