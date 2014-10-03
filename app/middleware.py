from django.shortcuts import redirect
#from django.contrib import messages

class Evalua:
    #def process_request(self, request):
        #if 'nombre' not in request.session and 'usuario' not in request.POST:
            #print 'Redireccionado'
            #return render_to_response('login.html',{}, context_instance=RequestContext(request))
            
    def process_view(self, request, view_func, view_args, view_kwargs):           
        if 'nombre' not in request.session and '/login/' not in request.path and '/validar/' not in request.path and '/admin/' not in request.path:
            #print 'no hay seccion middleware'
            #return redirect('/login')
            return
        #if 'adm' not in request.session['tipousuario'] and '/compras/' in request.path:
        #    return redirect('/')
        #messages.error(request, 'La session a caducado.')
        #return view_func(request, view_args, view_kwargs)