# from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader

from.models import Article, Comment

def articles(request):
    return render(request, 'news/articles.html',
        context={'articles' : Article.objects.all()})
    # template = loader.get_template('news/articles.html') # Loads the desired template
    # context = {'articles' : Article.objects.all()} # Creates a context that links the list of all articles with the 'articles' placeholder
    # return HttpResponse(template.render(context)) # Generates the final output of the template for the generated context

# def articles(request):   # request param is used to access certain info about the query
    # rows = []    # stores the text rows of the result
    # for m in Article.objects.all():  # iterates over all the articles in the database that we read with the model API and insert 5 rows per article in the rows list
        # rows.append("Article: '{}' from {}".format(
            # m.title, m.timestamp.strftime('%d/%m/%Y at %H:%M'))) # day/mo/year at hour/minute
        # rows.append('Text: {}'.format(m.text))
        # rows += ['', '-' * 30, '']   # adds a new line, a line with 30 `-`, and another blank line after the rows of text
    # response = HttpResponse('\n'.join(rows))  # joins and saves the http response as one block of text
    # response['Content-Type'] = 'text/plain'  # sets the content type of the http response to plain text
    # return response   # returns the response

def articles_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id) # Reads the article in question from the database as before or return a Http404 error

    """
    Checks if the `comment.save` has been passed via post to save a new comment if needed.
    If `comment.save` was not passed, the if block is ommitted and the detail page is displayed.
    """
    if 'save_comment' in request.POST:   
        name = request.POST.get('visitor_name', '')
        text = request.POST.get('comment_text', '')

        # Saves the comment text and the name of the user who commented, if the name and comment text were entered
        if name and text:
            comment = article.comment_set.create( # type: ignore
                author=name, text=text)
            comment.save()
            """
            HttpResponseRedirect redirects the visitor to the detail page instead of outputting a template, via GET and POST, upon a user refresh.
            It uses indirect redirection to prevent the retransmission of GET and POST data, and a copy of the users' comments being created
            when a refresh occurs. The GET and POST variables are discarded.
            """
            return HttpResponseRedirect('.')

        # Displays the detail page and an error if there is either comment text, but no name, or vice versa with no comment text and only name
        else:
            return render(request, 'news/articles_detail.html',
                context={'article': article,
                         'error': 'Input your name and a comment.',
                         'visitor_name' : name, 'comment_text' : text})
    return render(request, 'news/articles_detail.html',
        context={'article' : article})
    # article = get_object_or_404(Article, id=article_id)
    # return render(request, 'news/articles_detail.html',
        # context={'article' : article})

    # template = loader.get_template('news/articles_detail.html')
    # article = get_object_or_404(Article, id=article_id)
    # return HttpResponse(template.render({'article' : article}))

# def articles_detail(request, article_id):
    # try:
        # m = Article.objects.get(id=article_id)
    # except Article.DoesNotExist:
        # raise Http404
# 
    # rows = [
        # "Title: '{}' from {}".format(
            # m.title, m.timestamp.strftime('%d/%m/%Y at %H:%M')),
        # 'Text: {}'.format(m.text),
        # '', '-' * 30,
        # 'Comments:', '']
    # rows += ['{}: {}'.format(c.author, c.text)
                # for c in m.comment_set.all()] # type: ignore
    # response = HttpResponse('\n'.join(rows))
    # response['Content-Type'] = 'text/plain'
    # return response