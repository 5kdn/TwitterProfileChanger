#!/usr/bin/env node
// > yarn gulp [task_name]
const path = require('path');
const plumber = require('gulp-plumber');      // error handling
const notify  = require('gulp-notify');
const rootDir = './static/';

// load Gulp plugin
const gulp = require('gulp');


// = CONVERT PUG TO HTML =======================================================
// load Gulp-pug plugin
const pug = require('gulp-pug');

const pugFiles = ['pug/**/*.pug'];
const pugIgnore = ['!pug/**/_*'];
var pugTarget = pugFiles.concat(pugIgnore);

function convPug2Html() {
  gulp.src(pugTarget)
    .pipe(plumber({ errorHandler: notify.onError("Error: <%= error.message %>") }))
    .pipe(pug({
      // pug's setting
      pretty: true,
    }))
    .pipe(gulp.dest(rootDir));
}

// convert pug to html
gulp.task('html', convPug2Html());

gulp.task('html:watch', function () {
  gulp.watch(pugTarget, ['html']);
});

// = CONVERT SASS TO CSS =======================================================
// load Gulp-sass plugin
const sass = require('gulp-sass');

const sassFiles = ['scss/**/*.sass', 'scss/**/*.scss'];
const sassIgnore = ['!scss/**/_*'];
var sassTarget = sassFiles.concat(sassIgnore);

function convSass2Css(){
  gulp.src(sassTarget)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest( path.join(rootDir + 'css') ));
}

// convert sass to css file
gulp.task('css', convSass2Css());

gulp.task('css:watch', function(){
  gulp.watch(sassTarget, ['css']);
});

// = MINIFY JAVASCRIPT =========================================================
const uglify  = require('gulp-uglify');       // minify
const rename  = require('gulp-rename');       // rename

const jsFiles = ['script/**/*.js'];
const jsIgnore = ['!script/**/_*'];
var jsTarget = jsFiles.concat(jsIgnore);

function convJS(){
  gulp.src(jsTarget)
  .pipe(plumber())
  .pipe(uglify())
  .pipe(rename({
    extname: '.min.js'
  }))
  .pipe(gulp.dest(path.join(rootDir + '/js') ));
}

gulp.task('js', convJS());

gulp.task('js:watch', function () {
  gulp.watch(jsFiles, ['js']);
});
// = CONVERT ALL FILES =========================================================
gulp.task('convertAll', () =>{
  convPug2Html();
  convSass2Css();
  convJS();
});

// = RELOAD BROWSER ============================================================
gulp.task('reloadBrowser', function(){
  browserSync.reload();
});

// = WATCH FILES  AS DEFAULT ===================================================

gulp.task('default', function () {
  gulp.watch(['html', 'css', 'js', 'browserReload']);
});
