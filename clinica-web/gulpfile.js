var gulp = require("gulp");
var browserSync = require("browser-sync").create();
//connect = require('gulp-connect');

gulp.task("serve", function() {
	console.log("server staring...");
	browserSync.init({
		server: {
			//baseDir: "./"
			root: '.',
			livereload: true,
			port:3001
		}
	});
	gulp.watch("./index.html").on("change", browserSync.reload);
	gulp.watch("./login.html").on("change", browserSync.reload);
});