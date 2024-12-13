import AjaxService from 'ember-ajax/services/ajax';
import { computed } from '@ember/object';
import { getOwner } from '@ember/application';

export default class CustomAjaxService extends AjaxService {
  host = computed(function() {
    return getOwner(this).resolveRegistration('config:environment').APP.API_HOST;
  });
}
