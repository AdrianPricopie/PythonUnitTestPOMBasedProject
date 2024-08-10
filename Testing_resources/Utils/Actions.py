def ScrollToAnElement(self, locator):
    element = self.driver.find_element(locator)
    self.driver.execute_script("arguments[0].scrollIntoView();", element)