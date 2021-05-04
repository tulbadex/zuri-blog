

class CommentForm(forms.ModelForm):
    model = Comment 
    fields = ['comment']
    widgets = { 'body': forms.Textarea(attrs={'class':'form-control'})}