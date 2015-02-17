from bottle import route,run,post,static_file,request,template, debug,response
import bottle
from QueryGenerator import QueryGenerator
from pylab import *
import datetime
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

# Bottle Micro Framework
# SimpleTemplate Engine template
# Simple routing, easy access to form fields. Supports other templates like mako, Jinja2

@route('/')
def index():
    return template('pin_bar_result.tpl')

@route('/home')
def index():
    return template('pin_map_result.tpl')

@post('/query-interval')
def do_query():
      start_date=request.forms.get('startDate')
      end_date=request.forms.get('endDate')
      start_time=request.forms.get('startTime')
      end_time=request.forms.get('endTime')
      query=QueryGenerator(start_date,end_date,start_time,end_time)
      incidents=query.get_resultset()
      return template('pin_map_result.tpl',incidents=incidents)

@post('/sample-graph')
def do_graph():
      start_date=request.forms.get('startDate')
      end_date=request.forms.get('endDate')
      start_time=request.forms.get('startTime')
      end_time=request.forms.get('endTime')
      query=QueryGenerator(start_date,end_date,start_time,end_time)
      result=query.bar_resultset()
      location=[]
      count=[]
      fig=Figure()
      for index in result:
          location.append(index['Incident_type'])
          count.append(index['count'])
      pos=arange(len(location))+2
      barh(pos,count,align='center',color='#b8ff5c')
      yticks(pos,location)
      subplots_adjust(left=.40, right=.98)
      xticks([0,10,20,30,40,50])

      xlabel('Number of Incidents')
      ylabel('Type')
      title('Crime Rate in Waterloo')
      grid(True)
      return template(show())
      '''canvas=FigureCanvas(fig)
      response=bottle.BaseResponse(content_type='image/png')
      canvas.print_png(response)
      return response'''

# Server running 
run(host='localhost', port=8080, debug=True)

                         
