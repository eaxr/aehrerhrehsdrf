import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { AppComponent }   from './app.component'; 

import { HttpClientModule }   from '@angular/common/http';
import { Routes, RouterModule } from '@angular/router'; 
import { HomeComponent } from './home.component';
import { NotesListComponent } from './notes_list.component';
import { NotesNewComponent } from './notes_new.component';
import { NgxPaginationModule } from 'ngx-pagination';

const appRoutes: Routes =[
  { path: '', component: HomeComponent },
  { path: 'notesList', component: NotesListComponent },
  { path: 'noteNew', component: NotesNewComponent }
];

@NgModule({
  imports: [ 
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    NgxPaginationModule
  ],

  declarations: [ AppComponent, HomeComponent, NotesListComponent, NotesNewComponent],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
