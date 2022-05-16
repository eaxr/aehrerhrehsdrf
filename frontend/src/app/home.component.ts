import { Component, OnInit } from '@angular/core';
import { NotesService } from './service/notes.service';
import { throwError } from 'rxjs';
import { Note } from './notes';

@Component({
  selector: 'app-root',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
}
