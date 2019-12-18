def click_nth_element(self, selector, number, by=By.CSS_SELECTOR):
    """ Finds all matching page elements and clicks the nth visible one.
        Example:  self.click_nth_visible_element('[type="checkbox"]', 5)
                    (Clicks the 5th visible checkbox on the page.) """
    elements = self.find_elements(selector, by=by)
    if len(elements) < number:
        raise Exception("Not enough matching {%s} elements of type {%s} to"
                        " click number %s!" % (selector, by, number))
    number = number - 1
    if number < 0:
        number = 0
    element = elements[number]
    self.wait_for_ready_state_complete()
    try:
        self.__scroll_to_element(element)
        element.click()
    except (StaleElementReferenceException, ENI_Exception):
        self.wait_for_ready_state_complete()
        time.sleep(0.05)
        self.__scroll_to_element(element)
        element.click()