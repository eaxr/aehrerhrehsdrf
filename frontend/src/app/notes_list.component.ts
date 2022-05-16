import { Component, OnInit } from '@angular/core';
import { NotesService } from './service/notes.service';
import { throwError } from 'rxjs';
import { Note } from './notes';


@Component({
  selector: 'app-root',
  templateUrl: './notes_list.component.html',
  styleUrls: ['./notes_list.component.css']
})
export class NotesListComponent implements OnInit {

  public notesList: Note[] = [];
  page: number = 0;

  constructor(private _notesService: NotesService) { }

  ngOnInit() {
    this.getNotes();
  }

  getNotes() {
    this._notesService.getNotes().subscribe(res => {
      this.notesList = res;
    });
  }
}
