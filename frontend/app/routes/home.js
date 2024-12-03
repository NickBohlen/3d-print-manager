import Route from '@ember/routing/route';

export default class HomeRoute extends Route {
  async model() {
    const response = await fetch('http://127.0.0.1:8000/projects/api/projects/');
    const projects = await response.json();
    return projects;
  }
}
