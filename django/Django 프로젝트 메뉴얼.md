# Django 프로젝트 메뉴얼

### 1. 구조생성

- cmd창에서 프로젝트를 만들곳에서 `django-admin startproject [프로젝트이름]`을 입력한다. 그러면 프로젝트 관련되 뼈대 파일들이 생성된다.
- setting.py에 들어가서`LANGUAGE_CODE`를 `'ko-kr'`로 바꿔주고 `TIME_ZONE` 을 `'Asia/Seoul'`로 바꿔준다.
- cmd에 `python manage.py migrate`을 입력해서 데이터베이스를 만들어준다.
- python manage.py createsuperuser 를 입력해서 관리자 계정을 만들어준다.
- python manage.py startapp을 입력해서 app을 만들어준다. 
- setting.py에 들어가서 ` INSTALLED_APPS`에 설치한 app들을 추가한다. 예를 들어 이런식으로 `'puppy.apps.PuppyConfig',` 



### 2. 모델코딩

-  models.py에 모델 객체를 코딩해준다.

  ```
  class Bookmark(models.Model):
      title = models.CharField(max_length=100, blank=True, null=True)
      url = models.URLField('url', unique=True)
  
      def __str__(self):
          return self.title
  ```

  이런 느낌으로.

- admin.py에서 models를 import를 해줘서 app모델을 불러온다. 그리고 admin.site.register([app이름], [app이름admin])을 적어줘서 admin사이트에 등록을 해준다. `admin.site.register(Puppy)` 이런느낌으로. 그리고 만약 admin페이지에서 모델의 일부 정보를 보고싶으면 아래처럼 class를 추가해서 붙여준다.class 

  ```
  class BookmarkAdmin(admin.ModelAdmin):
  	list_display = ('title', 'url')
  	
  admin.site.register(Bookmark, BookmarkAdmin
  ```

  이런느낌.

-  python manage.py makemigrations 를 통해서 데이터베이스에 적용할 파일?을 만들어준다.
- python manage.py migrate를 통해서 데이터베이스를 업데이트시켜준다.



### 3. URLconf 코딩

- urls.py에 path를 지정해준다. 이때 URL을 관리하기 쉽게 app에 관련된 url은 app폴더 안에 ulrs.py를 새로 만들어줘서 path를 지정해준다.

  이때 django.urls에서 include를 불러와서 프로젝트 urls.py에서 app의 urls.py를 include해줘야한다. 

  예를 들어 아래와 같이 한다.

  프로젝트urls.py 

  ```
  path('bookmark/', include('bookmark.urls', namespace='bookmark')),
  ```

  app의 urls.py

  ```
  from django.conf.urls import url
  from django.urls import path
  from bookmark.views import BookmarkLV, BookmarkDV
  
  app_name = 'bookmark'
  
  urlpatterns = [
      path('', BookmarkLV.as_view(), name='index'),
      path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
  ]
  ```

  이런느낌.

  path를 넣어줄 때 view를 연결해주기위해서 import하는것을 잘 확인해야한다.

  - 클래스형 뷰는 클래스로 진입하기 위한 진입메소드를 제공하는데 , 이것이` as_view()`메소드이며, 아래의 순서로 요청을 처리한다. 

    `as_view()메`소드에서 클래스의 인스턴스를 생성한다. 

    생성된 인스턴스의 dispatch()메소드를 호출한다. 

    dispatch()메소드는 요청을 검사해서 HTTP의 메소드(GET, POST)를 알아낸다. 

    인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계한다.

    해당 메소드가 정의되어 있지 않으면, HttpResponseNotAllowd 예외를 발생시킨다.

  



### 4. 뷰코딩

- views.py를 코딩해줘야하는데 아래와 같이 해준다.

  ```
  from django.views.generic import ListView, DetailView
  from bookmark.models import Bookmark
  
  #--- ListView
  class BookmarkLV(ListView):
  	model = Bookmark
  
  #--- DetailView
  class BookmarkDV(DetailView):
  	model = Bookmark
  ```

  이런느낌.

  맨 위에는 geneircview를 불러오는데 **제네릭 뷰**는
  뷰 개발 과정에서 공통적으로 사용할 수 있는 기능들을 추상화하고, 장고에서 기본적으로 제공해주는 클래스형 뷰다.

  그 아래는 모델을 불러와준것.



### 5. 템플릿코딩

- 템플릿을 만들어줄때 모든 템플릿들이 공통으로 가져야하는 base.html이 필요할 수 있다. 이럴 때는 최상위 프로젝트 폴더에 templates폴터를 만들어주고 그 안에 base.html을 만들어준다. 그리고 이를 적용하기 위해서는 urls.py와 views.py를 차상위프로젝트 폴더 안에 있는거를 고쳐주고  setting.py를 수정해주어야한다.

  TEMPLATES = [

   {

  ​    'BACKEND': 'django.template.backends.django.DjangoTemplates',

  ​	**'DIRS': [`os.path.join(BASE_DIR, 'templates')`],**

  ​    'APP_DIRS': True,

  ​    'OPTIONS': {

  ​      'context_processors': [

  ​        'django.template.context_processors.debug',

  ​        'django.template.context_processors.request',

  ​        'django.contrib.auth.context_processors.auth',

  ​        'django.contrib.messages.context_processors.messages',

  ​      ],

  ​    },

    },

  ]

  표시한 부분을 입력해주어야 한다.

- templetes/[app이름]디렉토리 아래에 html파일을 만들어줘서 view에서 처리한 내용을 처리해준다. 설명을 달고싶은데 그냥 html을 잘만드는 수밖에 없다. 예시로 그냥 파일내용 하나 첨부하겠다.

  ```
  {% extends "base.html"%}
  {%block title%}Django Blog List{%endblock%}
  
  {% block content%}
  <div id=content>
  <h1>Blog List</h1>
  <!-- display blog list -->
  {% for post in posts %}
      <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
      {{ post.modify_date|date:"Y-m-d H:i" }}
      <p>{{ post.description }}</p>
  {% endfor %}
  <br/>
  </div>
  <!-- paging link -->
  <div>
      {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
      {% endif %}
      
      [ Page {{ page_obj.number }} / {{ page_obj.paginator.num_pages}} ]
  
      {% if page_obj.has_next %}
          <a href="?page={{ page_obj.next_page_number }}">Next</a>
      {% endif %}
  </div>
  {%endblock%}
  ```

  이런느낌?

- 템플릿에서 static을 불러오기 위해서는 `{%load static%}`을 통해서 static폴더를 불러와야한다. 안그러면 에러가 난다. 



### 6. 그 외

- static 디렉토리에서 정적인 데이터를 처리해준다. 예를들어 이미지등을 저장해두고 setting.py를 바꿔줘서 html에 정적인 파일을 불러올 수 있도록 해준다.

  static 폴더에 파일들을 넣고 사용하기 위해서는 settings.py 에 하나의 셋팅을 추가해 주어야 한다. 즉, settings.py 파일에서 아래와 같이 static 파일들을 찾는 경로를 나타내는 `STATICFILES_DIRS` 라는 변수를 설정해야 한다. 경로가 여러 개일 수 있지만, 여기서는 `BASE_DIR/static` 폴더 하나를 지정하였다.

  `import os`를 통해 불러오고 

  `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` 이렇게 입력해준다.

  html에서 이런식으로 불러올 수 있다.

  `<img src="{% static 'img/django-actor-big.jpg' %}" style="height:400px;"/>`

