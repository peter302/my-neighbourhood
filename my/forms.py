class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'content', 'image']
