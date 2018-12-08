context('Actions', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/ratings')
  })

  it('should be able to give positive rating with comment', () => {
    cy.contains('How do we do?')
    cy.get('img').should('have.attr', 'attr', 'Positive')
    cy.get('img').should('have.attr', 'attr', 'Neutral')
    cy.get('img').should('have.attr', 'attr', 'Negative')

    cy.get('img[alt="Positive"]').click()
    cy.wait(1000)

    cy.contains('Any comment?')
    cy.get('input[name="comment"]').type('You are doing great!')
    cy.get('button').click()
    cy.wait(1000)

    cy.contains('Thank you')
  })
})
