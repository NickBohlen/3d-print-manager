import Route from '@ember/routing/route';

export default class ApplicationRoute extends Route {
  async model() {
    // Fetch materials from the backend API
    const response = await fetch('http://127.0.0.1:8000/api/materials/');
    const materials = await response.json();

    // Return the data as the model for the application
    return { materials };
  }

  setupController(controller, model) {
    // Pass the materials data to the controller
    super.setupController(controller, model);
    controller.set('materials', model.materials);
  }
}