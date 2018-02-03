#!/usr/bin/env node
// > yarn gulp [task_name]
const path = require('path');
const plumber = require('gulp-plumber');      // error handling
const notify  = require('gulp-notify');
const rootDir = './webroot/templates/';
// const rootDir = './static/';

// load Gulp plugin
const gulp = require('gulp');


// = CONVERT PUG TO HTML =======================================================
// load Gulp-pug plugin
const pug = require('gulp-pug');

const pugFiles = ['pug/**/*.pug'];
const pugIgnore = ['!pug/**/_*'];
var pugTarget = pugFiles.concat(pugIgnore);

gulp.task('html', () =>{
  return gulp.src(pugTarget)
    .pipe(plumber({ errorHandler: notify.onError("Error: <%= error.message %>") }))
    .pipe(pug({
      // pug's setting
      pretty: true,
    }))
    .pipe(gulp.dest(rootDir));
});

gulp.task('html:watch', ()=> {
  gulp.watch(pugFiles, ['html']);
});


// = CONVERT SASS TO CSS =======================================================
const sass = require('gulp-sass');

const sassFiles = ['scss/**/*.sass', 'scss/**/*.scss'];
const sassIgnore = ['!scss/**/_*'];
var sassTarget = sassFiles.concat(sassIgnore);

gulp.task('css', () =>{
  return gulp.src(sassTarget)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(path.join(rootDir + 'css')));
});

gulp.task('css:watch', ()=>{
  gulp.watch(sassFiles, ['css']);
});

// = MINIFY JAVASCRIPT =========================================================
const concat  = require('gulp-concat');       // rename
const uglify  = require('gulp-uglify');       // minify
const rename  = require('gulp-rename');       // rename

const jsFiles = ['script/**/*.js'];
const jsIgnore = ['!script/**/_*'];
var jsTarget = jsFiles.concat(jsIgnore);

gulp.task('js', function () {
  return gulp.src(jsTarget)
  .pipe(plumber())                // error
  .pipe(concat('script.js'))
  // .pipe(uglify())
  .pipe(rename('script.min.js'))
  .pipe(gulp.dest(path.join(rootDir, 'js/')));
});

gulp.task('js:watch', function () {
  gulp.watch(jsFiles, ['js']);
});



// = WATCH FILES  AS DEFAULT ===================================================

var allFiles = pugFiles.concat(sassFiles).concat(jsFiles);
gulp.task('default', () => {
  gulp.watch(allFiles, ['html', 'css', 'js']);
});
