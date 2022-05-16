import { Component, OnInit } from '@angular/core';
import { NotesService } from './service/notes.service';
import { throwError } from 'rxjs';
import { Note } from './notes';

@Component({
  selector: 'app-root',
  templateUrl: './notes_new.component.html',
  styleUrls: ['./notes_new.component.css']
})
export class NotesNewComponent implements OnInit {
  newNote: any;

  constructor(private _notesService: NotesService) { }

  ngOnInit() {
    this.newNote = [];
  }

  postNote(newNote: Note) {
    this._notesService.postNote(newNote);
    this.newNote.title = null;
    this.newNote.description = null;
  }
}
