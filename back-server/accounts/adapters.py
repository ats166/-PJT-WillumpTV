from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        print(f'user={user}')
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        profile_image = data.get("profile_image")
        nickname = data.get("nickname")
        age = data.get("age")
        
        if profile_image:
            user.profile_image = profile_image
        if nickname:
            user.nickname = nickname
        if age:
            user.age = age
            
        user.save()
        return user