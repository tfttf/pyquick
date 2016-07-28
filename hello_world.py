#Hello, World!Hello, World!
import sublime, sublime_plugin
import sys
import functools
import os

class TestLuaCommand(sublime_plugin.TextCommand):


	def run(self, edit):
		self.window = sublime.active_window()
		self.view.insert(edit, 1, "Hello, World!")
		r = sublime.Region(0,self.view.size())
		#sublime.Selection.add(r)
		sys.stdout.write("111started\n%d,%d" %(r.a,r.b))
		self.view.replace(edit, r, 'Hello, World!')
		#import spdb ; spdb.start()
		sys.stdout.write("%r" % self.view.file_name())


		#self.compile_scripts_key=settings.get("compile_scripts_key", "")
		#self.window.run_command("hide_panel")
		output="res/game.zip"
		self.window.run_command("hide_panel")
		on_done = functools.partial(self.on_done, "res\game.zip")
		v = self.window.show_input_panel("Output File:", output, on_done, None, None)
		sys.stdout.write("%r"%v)
		v.sel().clear()
		v.sel().add(sublime.Region(4, 8))

	def on_done(self, path, output):

		sys.stdout.write("on_done function run")
		#sys.stderr.write("%r"%output)
        arr = os.path.split("res/game.zip")
        path=arr[1]
        sys.stderr.write("%r=============="%(path))
        sys.stderr.write("111111")
        sys.stderr.write("222222")
        sys.stderr.write("333333")
