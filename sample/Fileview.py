        
def html(content):
    """Publishes given html content into the output."""
    display.display(display.HTML(content))

def css(content=None, url=None):
    """Publishes css content."""
    if url is not None:
        html('<link rel=stylesheet type=text/css href=%r></link>' % url)
    else:
        html('<style>' + content + '</style>')
        
def javascript(content=None, url=None, script_id=None):
    """Publishes javascript content into the output."""
    if (content is None) == (url is None):
        raise ValueError('exactly one of content and url should be none')
    if url is not None:
        # Note: display.javascript will try to download script from python
        # which is very rarely useful.
        html('<script src=%r></script>' % url)
        return
    if not script_id and 'sourceURL=' not in content:
        script_id = 'js_' + hashlib.md5(content.encode('utf8')).hexdigest()[:10]
    if script_id:
        content += '\n//# sourceURL=%s' % script_id
        display.display(display.Javascript(content))
