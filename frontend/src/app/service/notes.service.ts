import { Injectable } from '@angular/core';
import { Note } from '../notes';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';

import { map } from 'rxjs/operators'
import { catchError } from 'rxjs/operators';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class NotesService {
  constructor(private http: HttpClient) { }

  getNotes(): Observable<Note[]> {
    return this.http.get<Note[]>(environment.apiURL + '/notes');
  }

  postNote(note: Note) {
    let productsUrl = environment.apiURL + '/notes';
      let body = {"title": note.title, "description": note.description};            

      let httpOptions = {
        headers: new HttpHeaders({
          'Content-Type': 'application/json'
        })
      };

      return this.http.post(productsUrl, body, httpOptions).subscribe();
    }

}
